"""Typed agent state shared across graph nodes and the pipeline.

The state is a plain dataclass (not a pydantic model) so it can be mutated
cheaply by graph nodes and trivially converted to/from the ``dict`` shape that
langgraph expects via :meth:`AgentState.as_dict` / :meth:`AgentState.from_dict`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolCall:
    """A single tool invocation and its observation."""

    step: int
    tool: str
    tool_input: str
    observation: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "step": self.step,
            "tool": self.tool,
            "input": self.tool_input,
            "observation": self.observation,
        }


@dataclass
class Source:
    """A citation produced by a tool (retriever / web_search)."""

    title: str
    snippet: str
    origin: str  # which tool produced it, e.g. "retriever" / "web_search"

    def as_dict(self) -> dict[str, Any]:
        return {"title": self.title, "snippet": self.snippet, "origin": self.origin}


@dataclass
class AgentState:
    """Mutable working memory for one research run."""

    question: str
    plan: list[str] = field(default_factory=list)
    messages: list[str] = field(default_factory=list)  # scratchpad / reasoning trace
    tool_calls: list[ToolCall] = field(default_factory=list)
    sources: list[Source] = field(default_factory=list)
    steps: int = 0
    max_steps: int = 6
    final_answer: str | None = None

    # ------------------------------------------------------------------ #
    # helpers
    # ------------------------------------------------------------------ #
    def add_message(self, text: str) -> None:
        self.messages.append(text)

    def record_tool_call(
        self, tool: str, tool_input: str, observation: str
    ) -> ToolCall:
        call = ToolCall(
            step=self.steps, tool=tool, tool_input=tool_input, observation=observation
        )
        self.tool_calls.append(call)
        return call

    def add_source(self, title: str, snippet: str, origin: str) -> None:
        self.sources.append(Source(title=title, snippet=snippet, origin=origin))

    @property
    def is_done(self) -> bool:
        return self.final_answer is not None or self.steps >= self.max_steps

    @property
    def scratchpad(self) -> str:
        """The reasoning trace + observations rendered for the LLM prompt."""
        # Format must stay parseable by agent.llm helpers: "<tool>(<input>) -> <obs>".
        lines: list[str] = []
        for call in self.tool_calls:
            lines.append(f"{call.tool}({call.tool_input}) -> {call.observation}")
        return "\n".join(lines)

    # ------------------------------------------------------------------ #
    # serialization (langgraph passes plain dicts between nodes)
    # ------------------------------------------------------------------ #
    def as_dict(self) -> dict[str, Any]:
        return {
            "question": self.question,
            "plan": list(self.plan),
            "messages": list(self.messages),
            "tool_calls": [c.as_dict() for c in self.tool_calls],
            "sources": [s.as_dict() for s in self.sources],
            "steps": self.steps,
            "max_steps": self.max_steps,
            "final_answer": self.final_answer,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AgentState:
        state = cls(question=data["question"])
        state.plan = list(data.get("plan", []))
        state.messages = list(data.get("messages", []))
        state.tool_calls = [
            ToolCall(
                step=c["step"], tool=c["tool"], tool_input=c["input"], observation=c["observation"]
            )
            for c in data.get("tool_calls", [])
        ]
        state.sources = [
            Source(title=s["title"], snippet=s["snippet"], origin=s["origin"])
            for s in data.get("sources", [])
        ]
        state.steps = data.get("steps", 0)
        state.max_steps = data.get("max_steps", 6)
        state.final_answer = data.get("final_answer")
        return state
