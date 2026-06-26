from presidio_analyzer import PatternRecognizer
from presidio_analyzer import Pattern


aadhaar_pattern = Pattern(
    name="aadhaar_pattern",
    regex=r"\b[2-9]\d{3}\s?\d{4}\s?\d{4}\b",
    score=0.95
)

aadhaar_recognizer = PatternRecognizer(
    supported_entity="AADHAAR",
    patterns=[aadhaar_pattern]
)


pan_pattern = Pattern(
    name="pan_pattern",
    regex=r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    score=0.95
)

pan_recognizer = PatternRecognizer(
    supported_entity="PAN",
    patterns=[pan_pattern]
)

ifsc_pattern = Pattern(
    name="ifsc_pattern",
    regex=r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
    score=0.95
)

ifsc_recognizer = PatternRecognizer(
    supported_entity="IFSC",
    patterns=[ifsc_pattern]
)

account_pattern = Pattern(
    name="account_pattern",
    regex=r"\b\d{9,18}\b",
    score=0.80
)

account_recognizer = PatternRecognizer(
    supported_entity="BANK_ACCOUNT",
    patterns=[account_pattern]
)