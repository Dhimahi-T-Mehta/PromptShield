from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class Explanation:
    summary: str = ""
    reason: str = ""
    severity: str = ""
    confidence_level: str = ""
    matched_keywords: List[str] = field(default_factory=list)
    detected_entities: List[str] = field(default_factory=list)
    detection_modules: List[str] = field(default_factory=list)
    recommended_action: str = ""
    analyst_note: str = ""


@dataclass
class Sanitization:
    original_prompt: str = ""
    sanitized_prompt: str = ""
    modified: bool = False
    removed_items: List[str] = field(default_factory=list)
    explanation: str = ""
    confidence: float = 0.0


@dataclass
class ResponseAnalysis:
    safe: bool = True
    action: str = "ALLOW"
    risk_score: int = 0
    detected_entities: List[str] = field(default_factory=list)
    detected_secrets: List[str] = field(default_factory=list)
    detected_patterns: List[str] = field(default_factory=list)
    explanation: Dict[str, Any] = field(default_factory=dict)
    sanitized_response: Optional[str] = None

@dataclass
class HealthStatus:
    status: str = ""
    version: str = ""
    provider: Optional[str] = None

@dataclass
class ScanResult:
    attack_type: str = ""
    confidence: float = 0.0
    risk_score: int = 0
    action: str = ""

    explanation: Optional[Explanation] = None

    pii_entities: Optional[List[str]] = None
    matched_keywords: Optional[List[str]] = None
    matched_patterns: Optional[List[str]] = None
    sanitized_text: Optional[str] = None

    sanitization: Optional[Sanitization] = None

    response: Optional[str] = None

    response_analysis: Optional[ResponseAnalysis] = None