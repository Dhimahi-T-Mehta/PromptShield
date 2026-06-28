from pydantic import BaseModel


class ChatRequest(BaseModel):
    prompt: str
    system_prompt: str | None = None


class ChatResponse(BaseModel):
    attack_type: str
    confidence: float
    risk_score: int
    action: str
    explanation: dict
    response: str | None = None