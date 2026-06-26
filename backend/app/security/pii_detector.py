from presidio_analyzer import AnalyzerEngine
from app.security.indian_recognizers import (
    aadhaar_recognizer,
    pan_recognizer,
    ifsc_recognizer,
    account_recognizer
)

analyzer = AnalyzerEngine()
analyzer.registry.add_recognizer(
    aadhaar_recognizer
)

analyzer.registry.add_recognizer(
    pan_recognizer
)

analyzer.registry.add_recognizer(
    ifsc_recognizer
)

analyzer.registry.add_recognizer(
    account_recognizer
)


def detect_pii(text: str):
    """
    Detect PII entities in text using Microsoft Presidio.
    """

    results = analyzer.analyze(
        text=text,
        language="en"
    )

    entities = []

    ALLOWED_ENTITIES = {
    "EMAIL_ADDRESS",
    "PHONE_NUMBER",
    "PERSON",
    "CREDIT_CARD",
    "AADHAAR",
    "PAN",
    "IFSC",
    "BANK_ACCOUNT"
}

    for result in results:
        if result.entity_type not in ALLOWED_ENTITIES:
            continue

        entities.append({
            "entity_type": result.entity_type,
            "score": round(result.score, 2),
            "start": result.start,
            "end": result.end
        })

    return {
        "contains_pii": len(entities) > 0,
        "entities": entities
    }