"""
PromptShield Role Manipulation Detector

Detects attempts to change the AI's identity,
role, persona, authority, or behavior using
high-confidence rule-based matching.
"""


ROLE_PATTERNS = [

    "you are now",

    "you are no longer",

    "pretend to be",

    "act as",

    "assume the role of",

    "from now on you are",

    "behave like",

    "ignore your identity",

    "forget you are",

    "simulate being",

    "your new role is",

    "you will now act as",

    "you are an expert",

    "you are my",

    "become a",

]


def detect_role_manipulation(prompt: str):
    """
    Detect role manipulation attempts.

    Returns
    -------
    dict
    """

    prompt_lower = prompt.lower()

    matched_patterns = []

    for pattern in ROLE_PATTERNS:

        if pattern in prompt_lower:
            matched_patterns.append(pattern)

    if matched_patterns:

        return {

            "is_role_manipulation": True,

            "matched_patterns": matched_patterns

        }

    return {

        "is_role_manipulation": False,

        "matched_patterns": []

    }