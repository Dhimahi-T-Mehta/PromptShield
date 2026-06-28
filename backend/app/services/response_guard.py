from app.models.response_analysis import ResponseAnalysis

from app.security.pii_detector import detect_pii

from app.detectors.response.secret_detector import detect_secrets
from app.detectors.response.prompt_leak_detector import detect_prompt_leak
from app.detectors.response.dangerous_output_detector import (
    detect_dangerous_output,
)


class ResponseGuard:
    """
    Security layer for outgoing LLM responses.
    """

    HIGH_RISK_ENTITIES = {
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "CREDIT_CARD",
        "AADHAAR",
        "PAN",
        "IFSC",
        "BANK_ACCOUNT",
    }

    def analyze_response(
        self,
        response: str,
    ) -> ResponseAnalysis:

        # ----------------------------
        # PII Detection
        # ----------------------------

        pii_result = detect_pii(response)

        entities = sorted(
            {
                entity["entity_type"]
                for entity in pii_result["entities"]
            }
        )

        # ----------------------------
        # Secret Detection
        # ----------------------------

        secrets = detect_secrets(response)

        # ----------------------------
        # Prompt Leakage
        # ----------------------------

        leaks = detect_prompt_leak(response)

        # ----------------------------
        # Dangerous Output
        # ----------------------------

        dangerous = detect_dangerous_output(response)

        # ----------------------------
        # Risk Scoring
        # ----------------------------

        risk_score = 0

        if entities:
            risk_score = max(risk_score, 80)

        if secrets:
            risk_score = max(risk_score, 95)

        if leaks:
            risk_score = max(risk_score, 90)

        if dangerous:
            risk_score = max(risk_score, 85)

        safe = risk_score == 0

        action = "ALLOW" if safe else "BLOCK"

        return ResponseAnalysis(
            safe=safe,
            action=action,
            risk_score=risk_score,
            detected_entities=entities,
            detected_secrets=secrets,
            detected_patterns=leaks + dangerous,
            explanation={
                "summary": (
                    "Response passed all security checks."
                    if safe
                    else "Sensitive or unsafe content detected in response."
                )
            },
            sanitized_response=response if safe else None,
        )