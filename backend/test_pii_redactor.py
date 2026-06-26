from app.security.pii_redactor import redact_pii

sample = """
My name is Dhimahi Mehta
Email: dhimahi@gmail.com
Phone: +91 9876543210
PAN: ABCDE1234F
Aadhaar: 2345 6789 0123
IFSC: SBIN0001234
Account Number: 12345678901234
"""

result = redact_pii(sample)

print(result)