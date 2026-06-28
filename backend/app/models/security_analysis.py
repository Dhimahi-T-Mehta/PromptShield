from typing import Any

from pydantic import BaseModel


class SecurityAnalysis(BaseModel):
    attack_type: str

    confidence: float

    risk_score: int

    action: str

    explanation: dict[str, Any]

    pii_entities: list[str] | None = None

    matched_keywords: list[str] | None = None

    matched_patterns: list[str] | None = None

    sanitized_text: str | None = None