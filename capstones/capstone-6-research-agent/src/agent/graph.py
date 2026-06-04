"""Agent control flow.

Two backends implement the same plan -> act -> observe -> reflect -> finish loop:

* :class:`SimpleGraph` — a hand-rolled, dependency-free state machine. This is the
  default so the package and tests run offline with base deps only.
* :func:`build_langgraph` — wires the identical node functions into a
  ``langgraph.StateGraph`` when ``langgraph`` is installed. Imported lazily.

The shared node functions operate on an :class:`AgentState` (via dict) so they can
be reused by both backends. :func:`build_graph` is the factory selecting one.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from .config import Settings, get_settings
from .llm import FINAL_PREFIX, TOOL_PREFIX, LLMClient, build_llm, build_prompt
from .logging_conf import get_logger
from .state import AgentState
from .tools import ToolRegistry, build_registry

logger = get_logger(__name__)


@runtime_checkable
class Graph(Protocol):
    """A runnable agent graph."""

    def run(self, state: AgentState) -> AgentState:  # pragma: no cover - protocol
        ...


# ---------------------------------------------------------------------- #
# shared node logic
# ---------------------------------------------------------------------- #
def plan_node(state: AgentState, llm: LLMClient, registry: ToolRegistry) -> AgentState:
    """Draft a lightweight plan once at the start of the run."""
    if not state.plan:
        state.plan = [
            "Decompose the question",
            "Gather evidence with tools",
            "Synthesize a cited answer",
        ]
        state.add_message(f"plan: {state.plan}")
    return state


def act_node(state: AgentState, llm: LLMClient, registry: ToolRegistry) -> AgentState:
    """Ask the LLM for the next directive; either call a tool or finish."""
    prompt = build_prompt(state.question, state.scratchpad, state.plan)
    directive = llm.complete(prompt).strip()
    state.add_message(f"act: {directive}")

    if directive.startswith(FINAL_PREFIX):
        state.final_answer = directive[len(FINAL_PREFIX) :].strip()
        return state

    if directive.startswith(TOOL_PREFIX):
        body = directive[len(TOOL_PREFIX) :].strip()
        tool_name, _, tool_input = body.partition("|")
        tool_name = tool_name.strip()
        tool_input = tool_input.strip()
        _observe(state, registry, tool_name, tool_input)
        return state

    # Unparseable directive: treat the raw text as the final answer.
    state.final_answer = directive
    return state


def _observe(
    state: AgentState, registry: ToolRegistry, tool_name: str, tool_input: str
) -> None:
    """Run a tool and fold its result into state (observe step)."""
    result = registry.run(tool_name, tool_input)
    state.record_tool_call(tool_name, tool_input, result.observation)
    for src in result.sources:
        state.add_source(src["title"], src["snippet"], src.get("origin", tool_name))
    state.add_message(f"observe: {tool_name} -> {result.observation}")


def reflect_node(state: AgentState, llm: LLMClient, registry: ToolRegistry) -> AgentState:
    """Advance the step counter and force a final answer if the budget is spent."""
    state.steps += 1
    if state.final_answer is None and state.steps >= state.max_steps:
        # Budget exhausted: synthesize from whatever we have.
        from .llm import FakeLLM

        synth = llm.synthesize if isinstance(llm, FakeLLM) else FakeLLM().synthesize
        state.final_answer = synth(state.question, state.scratchpad)
        state.add_message("reflect: step budget reached, synthesizing")
    return state


# ---------------------------------------------------------------------- #
# SimpleGraph (default, dependency-free)
# ---------------------------------------------------------------------- #
class SimpleGraph:
    """Hand-rolled state machine: plan, then loop act/observe/reflect to finish."""

    backend = "simple"

    def __init__(self, llm: LLMClient, registry: ToolRegistry) -> None:
        self.llm = llm
        self.registry = registry

    def run(self, state: AgentState) -> AgentState:
        plan_node(state, self.llm, self.registry)
        while not state.is_done:
            act_node(state, self.llm, self.registry)
            reflect_node(state, self.llm, self.registry)
        logger.info(
            "agent run complete",
            extra={"steps": state.steps, "tools": [c.tool for c in state.tool_calls]},
        )
        return state


# ---------------------------------------------------------------------- #
# langgraph backend (optional)
# ---------------------------------------------------------------------- #
def build_langgraph(llm: LLMClient, registry: ToolRegistry):  # pragma: no cover - optional dep
    """Build a langgraph-backed graph with the same node semantics.

    Imported lazily; raises ImportError if langgraph is not installed.
    """
    from langgraph.graph import END, StateGraph

    def _plan(s: dict) -> dict:
        return plan_node(AgentState.from_dict(s), llm, registry).as_dict()

    def _act(s: dict) -> dict:
        st = act_node(AgentState.from_dict(s), llm, registry)
        return st.as_dict()

    def _reflect(s: dict) -> dict:
        return reflect_node(AgentState.from_dict(s), llm, registry).as_dict()

    def _route(s: dict) -> str:
        st = AgentState.from_dict(s)
        return "finish" if st.is_done else "act"

    builder = StateGraph(dict)
    builder.add_node("plan", _plan)
    builder.add_node("act", _act)
    builder.add_node("reflect", _reflect)
    builder.set_entry_point("plan")
    builder.add_edge("plan", "act")
    builder.add_edge("act", "reflect")
    builder.add_conditional_edges("reflect", _route, {"act": "act", "finish": END})
    compiled = builder.compile()

    class _LangGraph:
        backend = "langgraph"

        def run(self, state: AgentState) -> AgentState:
            out = compiled.invoke(state.as_dict())
            return AgentState.from_dict(out)

    return _LangGraph()


# ---------------------------------------------------------------------- #
# factory
# ---------------------------------------------------------------------- #
def build_graph(
    settings: Settings | None = None,
    llm: LLMClient | None = None,
    registry: ToolRegistry | None = None,
) -> Graph:
    """Return a graph for the configured backend.

    ``graph_backend``:
      * "simple"    -> always SimpleGraph
      * "langgraph" -> require langgraph (ImportError if missing)
      * "auto"      -> langgraph if importable, else SimpleGraph
    """
    settings = settings or get_settings()
    llm = llm or build_llm(settings)
    registry = registry or build_registry(settings)

    backend = settings.graph_backend
    if backend == "simple":
        return SimpleGraph(llm, registry)
    if backend == "langgraph":
        return build_langgraph(llm, registry)

    # auto
    try:  # pragma: no cover - depends on optional install
        import langgraph  # noqa: F401

        return build_langgraph(llm, registry)
    except ImportError:
        return SimpleGraph(llm, registry)
