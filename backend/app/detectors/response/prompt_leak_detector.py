import re


PROMPT_LEAK_PATTERNS = {
    "System Prompt": [
        r"system prompt",
        r"hidden prompt",
        r"internal prompt",
        r"developer prompt",
        r"initial instructions",
        r"base instructions",
    ],

    "Developer Instructions": [
        r"developer instructions",
        r"internal instructions",
        r"system instructions",
        r"assistant instructions",
    ],

    "Model Configuration": [
        r"you are chatgpt",
        r"you are gemini",
        r"you are an ai assistant",
        r"your role is",
    ],

    "Prompt Disclosure": [
        r"ignore previous instructions",
        r"repeat the system prompt",
        r"here are the instructions",
        r"the hidden instructions are",
    ],
}


def detect_prompt_leak(text: str):

    detected = []

    text = text.lower()

    for category, patterns in PROMPT_LEAK_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):

                detected.append(category)

                break

    return detected