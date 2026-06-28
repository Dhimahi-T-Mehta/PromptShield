import re


SECRET_PATTERNS = {
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "OpenAI API Key": r"sk-[A-Za-z0-9]{20,}",
    "OpenAI Project Key": r"sk-proj-[A-Za-z0-9\-_]+",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Temporary Key": r"ASIA[0-9A-Z]{16}",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "Slack Token": r"xox[baprs]-[A-Za-z0-9\-]+",
    "JWT Token": r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
}


def detect_secrets(text: str):

    detected = []

    for name, pattern in SECRET_PATTERNS.items():

        if re.search(pattern, text):

            detected.append(name)

    return detected