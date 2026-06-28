from typing import Any

from pydantic import BaseModel, Field


class ResponseAnalysis(BaseModel):
    """
    Analysis result for an outgoing LLM response.
    """

    safe: bool

    action: str

    risk_score: int

    detected_entities: list[str] = Field(default_factory=list)

    detected_secrets: list[str] = Field(default_factory=list)

    detected_patterns: list[str] = Field(default_factory=list)

    explanation: dict[str, Any] = Field(default_factory=dict)

    sanitized_response: str | None = None