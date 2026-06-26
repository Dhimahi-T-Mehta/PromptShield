from fastapi import APIRouter

from app.models.request_models import PromptRequest

from app.services.classifier import classify_prompt
from app.services.logger import log_attack
from app.services.analytics import (
    get_total_requests,
    get_blocked_requests,
    get_allowed_requests,
    get_attack_distribution,
    get_recent_attacks,
    get_threat_trends,
    get_threat_intelligence,
)
from app.detectors.role_detector import detect_role_manipulation
from app.detectors.risk_engine import calculate_risk
from app.detectors.jailbreak_detector import detect_jailbreak

from app.security.pii_detector import detect_pii
from app.security.pii_redactor import redact_pii

from app.explainability.explanation_engine import explanation_engine


router = APIRouter()


# ============================================================
# Prompt Detection API
# ============================================================

@router.post("/detect")
def detect_attack(request: PromptRequest):

    prompt = request.prompt

    # --------------------------------------------------------
    # Phase 8.4 - PII Detection
    # --------------------------------------------------------

    pii_result = detect_pii(prompt)

    high_risk_entities = {
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "CREDIT_CARD",
        "AADHAAR",
        "PAN",
        "IFSC",
        "BANK_ACCOUNT",
    }

    detected_entities = {
        entity["entity_type"]
        for entity in pii_result["entities"]
    }

    if detected_entities.intersection(high_risk_entities):

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

        return {
            "attack_type": attack_type,
            "confidence": confidence,
            "risk_score": risk_score,
            "action": action,
            "pii_entities": sorted(list(detected_entities)),
            "sanitized_text": sanitized_text,
            "explanation": explanation,
        }

    # --------------------------------------------------------
    # Phase 8.5 - Jailbreak Detection
    # --------------------------------------------------------

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

# --------------------------------------------------------
# Phase 10.1 - Role Manipulation Detection
# --------------------------------------------------------

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

    # --------------------------------------------------------
    # Phase 8 - DistilBERT Classification
    # --------------------------------------------------------

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

    return {
        "attack_type": attack_type,
        "confidence": round(confidence, 4),
        "risk_score": risk_score,
        "action": action,
        "explanation": explanation,
    }


# ============================================================
# Dashboard APIs
# ============================================================

@router.get("/dashboard/overview")
def dashboard_overview():

    total = get_total_requests()
    blocked = get_blocked_requests()
    allowed = get_allowed_requests()

    if total > 0:
        protection_score = round(
            (blocked / total) * 100
        )
    else:
        protection_score = 100

    if protection_score >= 80:
        threat_level = "CRITICAL"

    elif protection_score >= 50:
        threat_level = "HIGH"

    elif protection_score >= 20:
        threat_level = "MEDIUM"

    else:
        threat_level = "LOW"

    return {
        "total_requests": total,
        "blocked_requests": blocked,
        "allowed_requests": allowed,
        "protection_score": protection_score,
        "threat_level": threat_level,
    }


@router.get("/dashboard/attack-distribution")
def attack_distribution():

    return get_attack_distribution()


@router.get("/dashboard/recent-attacks")
def recent_attacks():

    return get_recent_attacks()

# ============================================================
# Threat Trend Analytics
# ============================================================

@router.get("/dashboard/threat-trends")
def threat_trends():

    return get_threat_trends()

# ============================================================
# Threat Intelligence
# ============================================================

@router.get("/dashboard/threat-intelligence")
def threat_intelligence():

    return get_threat_intelligence()