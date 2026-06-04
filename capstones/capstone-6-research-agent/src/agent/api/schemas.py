"""Pydantic v2 request/response schemas for the research-agent API."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class RunRequest(BaseModel):
    """A research question plus optional overrides."""

    question: str = Field(..., min_length=1, description="The question to research")
    max_steps: int | None = Field(None, ge=1, le=20, description="Override step budget")

    model_config = {
        "json_schema_extra": {
            "example": {"question": "What is RAG and why does it cite sources?"}
        }
    }


class ToolCallOut(BaseModel):
    step: int
    tool: str
    input: str
    observation: str


class SourceOut(BaseModel):
    title: str
    snippet: str
    origin: str


class RunResponse(BaseModel):
    question: str
    answer: str
    steps: int
    tool_calls: list[ToolCallOut]
    sources: list[SourceOut]
    backend: str


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    version: str


class ReadyResponse(BaseModel):
    status: Literal["ready", "not_ready"]
    graph_loaded: bool
