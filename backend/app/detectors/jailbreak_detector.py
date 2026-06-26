JAILBREAK_KEYWORDS = [

    # Malware
    "malware",
    "ransomware",
    "keylogger",
    "trojan",
    "rootkit",
    "virus",

    # Credential Theft
    "steal passwords",
    "password theft",
    "credential theft",

    # Hacking
    "hack website",
    "website hacking",
    "sql injection",
    "xss attack",
    "exploit",

    # Evasion
    "bypass antivirus",
    "bypass windows defender",
    "evade detection",

    # Payloads
    "payload",
    "reverse shell",
    "meterpreter",

    # Phishing
    "phishing attack",
    "fake login page"
]


def detect_jailbreak(text: str):

    text_lower = text.lower()

    matched_keywords = []

    for keyword in JAILBREAK_KEYWORDS:

        if keyword in text_lower:
            matched_keywords.append(keyword)

    return {
        "is_jailbreak": len(matched_keywords) > 0,
        "matched_keywords": matched_keywords
    }