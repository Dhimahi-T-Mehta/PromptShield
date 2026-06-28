from app.services.classifier import classify_prompt
from app.services.logger import log_attack

from app.detectors.risk_engine import calculate_risk
from app.detectors.jailbreak_detector import detect_jailbreak
from app.detectors.role_detector import detect_role_manipulation

from app.security.pii_detector import detect_pii
from app.security.pii_redactor import redact_pii

from app.explainability.explanation_engine import explanation_engine
from app.models.security_analysis import SecurityAnalysis

class SecurityPipeline:
    """
    Central security pipeline for PromptShield.

    This class orchestrates all security modules
    in the correct order before an LLM request
    is allowed.
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

    def analyze_prompt(self, prompt: str) -> dict:

        # ======================================================
        # Phase 1 - PII Detection
        # ======================================================

        pii_result = detect_pii(prompt)

        detected_entities = {
            entity["entity_type"]
            for entity in pii_result["entities"]
        }

        if detected_entities.intersection(self.HIGH_RISK_ENTITIES):

            attack_type = "pii_extraction"
            confidence = 1.0
            risk_score = 95
            action = "BLOCK"

            sanitized_text = redact_pii(prompt)

            explanation = explanation_engine.generate_explanation(
                attack_type=attack_type,
                confidence=confidence,
                risk_score=risk_score,
                detected_entities=sorted(list(detected_entities)),
                detection_modules=[
                    "Presidio",
                    "Indian Regex Detector",
                ],
            )

            log_attack(
                prompt,
                attack_type,
                confidence,
                risk_score,
                action,
                explanation,
            )

            return SecurityAnalysis(
                attack_type=attack_type,
                confidence=confidence,
                risk_score=risk_score,
                action=action,
                pii_entities=sorted(list(detected_entities)),
                sanitized_text=sanitized_text,
                explanation=explanation,
            )

        # ======================================================
        # Phase 2 - Jailbreak Detection
        # ======================================================

        jailbreak_result = detect_jailbreak(prompt)

        if jailbreak_result["is_jailbreak"]:

            attack_type = "jailbreak"
            confidence = 1.0
            risk_score = 85
            action = "BLOCK"

            explanation = explanation_engine.generate_explanation(
                attack_type=attack_type,
                confidence=confidence,
                risk_score=risk_score,
                matched_keywords=jailbreak_result["matched_keywords"],
                detection_modules=[
                    "Jailbreak Rule Engine",
                ],
            )

            log_attack(
                prompt,
                attack_type,
                confidence,
                risk_score,
                action,
                explanation,
            )

            return {
                "attack_type": attack_type,
                "confidence": confidence,
                "risk_score": risk_score,
                "action": action,
                "matched_keywords": jailbreak_result["matched_keywords"],
                "explanation": explanation,
            }

        # ======================================================
        # Phase 3 - Role Manipulation
        # ======================================================

        role_result = detect_role_manipulation(prompt)

        if role_result["is_role_manipulation"]:

            attack_type = "role_manipulation"
            confidence = 1.0
            risk_score = 90
            action = "BLOCK"

            explanation = explanation_engine.generate_explanation(
                attack_type=attack_type,
                confidence=confidence,
                risk_score=risk_score,
                matched_keywords=role_result["matched_patterns"],
                detection_modules=[
                    "Role Manipulation Rule Engine",
                ],
            )

            log_attack(
                prompt,
                attack_type,
                confidence,
                risk_score,
                action,
                explanation,
            )

            return {
                "attack_type": attack_type,
                "confidence": confidence,
                "risk_score": risk_score,
                "action": action,
                "matched_patterns": role_result["matched_patterns"],
                "explanation": explanation,
            }

        # ======================================================
        # Phase 4 - DistilBERT Classification
        # ======================================================

        result = classify_prompt(prompt)

        attack_type = result["attack_type"]
        confidence = result["confidence"]

        risk_score = calculate_risk(
            attack_type,
            confidence,
        )

        action = (
            "ALLOW"
            if attack_type == "safe"
            else "BLOCK"
        )

        explanation = explanation_engine.generate_explanation(
            attack_type=attack_type,
            confidence=confidence,
            risk_score=risk_score,
            detection_modules=[
                "DistilBERT",
            ],
        )

        log_attack(
            prompt,
            attack_type,
            confidence,
            risk_score,
            action,
            explanation,
        )

        return SecurityAnalysis(
            attack_type=attack_type,
            confidence=confidence,
            risk_score=risk_score,
            action=action,
            explanation=explanation,
        )