from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

from app.security.indian_recognizers import (
    aadhaar_recognizer,
    pan_recognizer,
    ifsc_recognizer,
    account_recognizer
)

analyzer = AnalyzerEngine()

# Register custom Indian recognizers
analyzer.registry.add_recognizer(aadhaar_recognizer)
analyzer.registry.add_recognizer(pan_recognizer)
analyzer.registry.add_recognizer(ifsc_recognizer)
analyzer.registry.add_recognizer(account_recognizer)

anonymizer = AnonymizerEngine()


def redact_pii(text: str):
    """
    Detect and redact PII from text.
    """

    results = analyzer.analyze(
        text=text,
        language="en"
    )

    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )

    return anonymized_result.text