from fastapi import APIRouter
from app.services.security_pipeline import SecurityPipeline
from app.models.request_models import PromptRequest

from app.services.analytics import (
    get_total_requests,
    get_blocked_requests,
    get_allowed_requests,
    get_attack_distribution,
    get_recent_attacks,
    get_threat_intelligence,
    get_threat_trends,
    get_detection_module_stats,
)


router = APIRouter()
pipeline = SecurityPipeline()


# ============================================================
# Prompt Detection API
# ============================================================

@router.post("/detect")
def detect_attack(request: PromptRequest):
    """
    Analyze a prompt using the PromptShield Security Pipeline.
    """

    return pipeline.analyze_prompt(
        request.prompt
    )

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

@router.get("/dashboard/detection-modules")
def detection_module_statistics():
    """
    Returns statistics for each detection module.
    """

    return get_detection_module_stats()