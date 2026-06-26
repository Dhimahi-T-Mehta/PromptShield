from app.security.pii_detector import detect_pii


sample_text = """
My Aadhaar is 1234 5678 9012
"""

result = detect_pii(sample_text)

print(result)