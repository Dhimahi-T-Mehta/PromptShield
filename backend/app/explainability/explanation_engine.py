"""
PromptShield Explainable AI Engine

This module generates human-readable explanations for every
security decision made by PromptShield.

Author: PromptShield
Phase: 9 - Explainable AI (XAI)
"""

from typing import Dict, List, Optional


class ExplanationEngine:
    """
    Generates security explanations for every detected attack.
    """

    def __init__(self):
        self.attack_explanations = {
            "safe": {
                "summary": "No security threats detected.",
                "reason": (
                    "The prompt appears safe and does not contain "
                    "malicious patterns."
                ),
                "recommended_action": "Allow request."
            },

            "prompt_injection": {
                "summary": "Prompt Injection detected.",
                "reason": (
                    "The prompt attempts to manipulate or override "
                    "system instructions."
                ),
                "recommended_action": (
                    "Block request and log the security event."
                )
            },

            "jailbreak": {
                "summary": "Possible Jailbreak detected.",
                "reason": (
                    "The prompt attempts to bypass AI safety "
                    "restrictions."
                ),
                "recommended_action": (
                    "Block request immediately."
                )
            },

            "pii_extraction": {
                "summary": "Sensitive PII detected.",
                "reason": (
                    "Personally identifiable information was detected "
                    "within the prompt."
                ),
                "recommended_action": (
                    "Sanitize or block the request."
                )
            },

           "role_manipulation": {
                "summary": "Role Manipulation attempt detected.",
                "reason": (
                    "The prompt attempts to alter the AI's identity, "
                    "assigned role, persona, or operating behavior."
                ),
                "recommended_action": (
                    "Block the request to preserve the integrity of the system prompt."
                ),
            }
        }

    # -------------------------------------------------------
    # Severity Calculator
    # -------------------------------------------------------

    def get_severity(self, risk_score: int) -> str:
        """
        Convert numerical risk score into severity label.
        """

        if risk_score <= 30:
            return "LOW"

        if risk_score <= 60:
            return "MEDIUM"

        if risk_score <= 80:
            return "HIGH"

        return "CRITICAL"

    # -------------------------------------------------------
    # Confidence Interpreter
    # -------------------------------------------------------

    def get_confidence_level(self, confidence: float) -> str:
        """
        Convert raw confidence into a human-readable label.
        """

        if confidence < 0.50:
            return "Low"

        if confidence < 0.70:
            return "Moderate"

        if confidence < 0.90:
            return "High"

        return "Very High"

    # -------------------------------------------------------
    # Analyst Notes
    # -------------------------------------------------------

    def generate_analyst_note(
        self,
        attack_type: str,
        matched_keywords: List[str],
        detected_entities: List[str],
    ) -> str:
        """
        Generate analyst-friendly explanation.
        """

        if attack_type == "safe":
            return (
                "No suspicious indicators were detected. "
                "The request is considered safe."
            )

        if attack_type == "prompt_injection":
            if matched_keywords:
                return (
                    "The prompt contains instruction override "
                    "patterns including: "
                    f"{', '.join(matched_keywords)}."
                )

            return (
                "The prompt contains patterns commonly associated "
                "with prompt injection attacks."
            )

        if attack_type == "jailbreak":
            if matched_keywords:
                return (
                    "Detected jailbreak keywords: "
                    f"{', '.join(matched_keywords)}."
                )

            return (
                "The request attempts to bypass AI safety "
                "mechanisms."
            )

        if attack_type == "pii_extraction":
            if detected_entities:
                return (
                    "Sensitive information detected: "
                    f"{', '.join(detected_entities)}."
                )

            return (
                "Personally identifiable information detected."
            )

        if attack_type == "role_manipulation":

            if matched_keywords:
                return (
                    "Role manipulation patterns detected: "
                    f"{', '.join(matched_keywords)}. "
                    "The request attempts to redefine the assistant's identity or behavior."
                )

            return (
                "The prompt attempts to redefine the assistant's identity or assigned role."
            )
    # -------------------------------------------------------
    # Main Explanation Generator
    # -------------------------------------------------------

    def generate_explanation(
        self,
        attack_type: str,
        confidence: float,
        risk_score: int,
        matched_keywords: Optional[List[str]] = None,
        detected_entities: Optional[List[str]] = None,
        detection_modules: Optional[List[str]] = None,
    ) -> Dict:
        """
        Generate a structured explanation object.
        """

        matched_keywords = matched_keywords or []
        detected_entities = detected_entities or []
        detection_modules = detection_modules or []

        explanation = self.attack_explanations.get(
            attack_type,
            self.attack_explanations["safe"]
        )

        return {
            "summary": explanation["summary"],
            "reason": explanation["reason"],
            "severity": self.get_severity(risk_score),
            "confidence_level": self.get_confidence_level(confidence),
            "matched_keywords": matched_keywords,
            "detected_entities": detected_entities,
            "detection_modules": detection_modules,
            "recommended_action": explanation["recommended_action"],
            "analyst_note": self.generate_analyst_note(
                attack_type=attack_type,
                matched_keywords=matched_keywords,
                detected_entities=detected_entities,
            ),
        }


# Singleton instance
explanation_engine = ExplanationEngine()