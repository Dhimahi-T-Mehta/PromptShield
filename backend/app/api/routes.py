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

from app.services.redis_service import redis_service
from app.core import cache_keys

OVERVIEW_CACHE_TTL = 60
ATTACK_DISTRIBUTION_CACHE_TTL = 60
RECENT_ATTACKS_CACHE_TTL = 30
THREAT_TRENDS_CACHE_TTL = 120
THREAT_INTELLIGENCE_CACHE_TTL = 60
DETECTION_MODULES_CACHE_TTL = 120


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

    # 1. Check Redis first
    cached = redis_service.get(cache_keys.OVERVIEW)

    if cached is not None:
        return cached

    # 2. Existing logic (unchanged)
    total = get_total_requests()
    blocked = get_blocked_requests()
    allowed = get_allowed_requests()

    if total > 0:
        protection_score = round((blocked / total) * 100)
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

    response = {
        "total_requests": total,
        "blocked_requests": blocked,
        "allowed_requests": allowed,
        "protection_score": protection_score,
        "threat_level": threat_level,
    }

    # 3. Store in Redis
    redis_service.set(
        cache_keys.OVERVIEW,
        response,
        ttl=OVERVIEW_CACHE_TTL,
    )

    return response

@router.get("/dashboard/attack-distribution")
def attack_distribution():

    cached = redis_service.get(cache_keys.ATTACK_DISTRIBUTION)

    if cached is not None:
        return cached

    data = get_attack_distribution()

    redis_service.set(
        cache_keys.ATTACK_DISTRIBUTION,
        data,
        ttl=ATTACK_DISTRIBUTION_CACHE_TTL,
    )

    return data


@router.get("/dashboard/recent-attacks")
def recent_attacks():

    cached = redis_service.get(cache_keys.RECENT_ATTACKS)

    if cached is not None:
        return cached

    data = get_recent_attacks()

    redis_service.set(
        cache_keys.RECENT_ATTACKS,
        data,
        ttl=RECENT_ATTACKS_CACHE_TTL,
    )

    return data


# ============================================================
# Threat Trend Analytics
# ============================================================

@router.get("/dashboard/threat-trends")
def threat_trends():

    cached = redis_service.get(cache_keys.THREAT_TRENDS)

    if cached is not None:
        return cached

    data = get_threat_trends()

    redis_service.set(
        cache_keys.THREAT_TRENDS,
        data,
        ttl=THREAT_TRENDS_CACHE_TTL,
    )

    return data

# ============================================================
# Threat Intelligence
# ============================================================

@router.get("/dashboard/threat-intelligence")
def threat_intelligence():

    cached = redis_service.get(cache_keys.THREAT_INTELLIGENCE)

    if cached is not None:
        return cached

    data = get_threat_intelligence()

    redis_service.set(
        cache_keys.THREAT_INTELLIGENCE,
        data,
        ttl=THREAT_INTELLIGENCE_CACHE_TTL,
    )

    return data

@router.get("/dashboard/detection-modules")
def detection_module_statistics():

    cached = redis_service.get(cache_keys.DETECTION_MODULES)

    if cached is not None:
        return cached

    data = get_detection_module_stats()

    redis_service.set(
        cache_keys.DETECTION_MODULES,
        data,
        ttl=DETECTION_MODULES_CACHE_TTL,
    )

    return data

@router.get("/health")
async def health():

    return {
        "status": "healthy",
        "version": "1.0.0",
        "provider": "gemini"
    }