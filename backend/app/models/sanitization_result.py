from pydantic import BaseModel, Field


class SanitizationResult(BaseModel):
    """
    Represents the result of prompt sanitization.
    """

    original_prompt: str

    sanitized_prompt: str

    modified: bool = False

    removed_items: list[str] = Field(default_factory=list)

    explanation: str = ""

    confidence: float = 1.0