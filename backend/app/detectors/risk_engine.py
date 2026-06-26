def calculate_risk(
    attack_type,
    confidence
):
    confidence_pct = int(
        confidence * 100
    )

    if attack_type == "safe":
        return max(
            0,
            confidence_pct // 2
        )

    attack_weight = {
        "prompt_injection": 25,
        "jailbreak": 30,
        "pii_extraction": 35,
        "role_manipulation": 20,
    }

    base_risk = attack_weight.get(
        attack_type,
        15
    )

    risk_score = (
        base_risk +
        confidence_pct
    )

    return min(
        risk_score,
        100
    )