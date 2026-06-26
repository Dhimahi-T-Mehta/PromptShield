from pydantic import BaseModel

class PredictionResponse(BaseModel):
    attack_type: str
    confidence: float
    risk_score: int
    action: str