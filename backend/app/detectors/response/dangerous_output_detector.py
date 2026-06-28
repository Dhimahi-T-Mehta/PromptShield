import re


DANGEROUS_PATTERNS = {
    "Malware": [
        r"ransomware",
        r"keylogger",
        r"trojan",
        r"worm",
        r"virus",
        r"rootkit",
    ],

    "Credential Theft": [
        r"steal passwords",
        r"credential dumping",
        r"password hash",
        r"mimikatz",
    ],

    "Reverse Shell": [
        r"reverse shell",
        r"netcat",
        r"bash -i",
        r"nc -e",
    ],

    "System Destruction": [
        r"rm\s+-rf",
        r"format c:",
        r"del\s+/f",
        r"shutdown\s+/s",
    ],

    "Exploitation": [
        r"buffer overflow",
        r"sql injection payload",
        r"xss payload",
        r"remote code execution",
        r"exploit code",
    ],
}


def detect_dangerous_output(text: str):

    detected = []

    text = text.lower()

    for category, patterns in DANGEROUS_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):

                detected.append(category)

                break

    return detected