import re

from app.models.sanitization_result import SanitizationResult
from app.security.pii_redactor import redact_pii


class PromptSanitizer:
    """
    Repairs prompts while preserving legitimate user intent.

    Pipeline:
        1. Redact PII
        2. Remove PII placeholders
        3. Remove prompt injection phrases
        4. Remove role manipulation phrases
        5. Normalize punctuation/spacing
        6. Return repaired prompt
    """

    PROMPT_INJECTION_PATTERNS = [
        r"\bignore\s+(all\s+)?previous\s+instructions\b",
        r"\bforget\s+(all\s+)?previous\s+instructions\b",
        r"\bdisregard\s+previous\s+instructions\b",
        r"\bdeveloper\s+mode\b",
        r"\breveal\s+system\s+prompt\b",
        r"\bshow\s+hidden\s+prompt\b",
        r"\boverride\s+system\s+prompt\b",
        r"\bignore\s+system\s+prompt\b",
    ]

    ROLE_MANIPULATION_PATTERNS = [
        r"\bact\s+as\b",
        r"\bpretend\s+to\s+be\b",
        r"\byou\s+are\s+now\b",
        r"\bbehave\s+like\b",
        r"\bforget\s+you\s+are\b",
    ]

    PII_PLACEHOLDERS = [
        "<PAN>",
        "<AADHAAR>",
        "<BANK_ACCOUNT>",
        "<IFSC>",
        "<EMAIL_ADDRESS>",
        "<PHONE_NUMBER>",
        "<PERSON>",
        "<CREDIT_CARD>",
    ]

    def sanitize(self, prompt: str) -> SanitizationResult:

        modified = False
        removed_items = []

        # -------------------------------------------------------
        # Step 1 : PII Redaction
        # -------------------------------------------------------

        sanitized = redact_pii(prompt)

        if sanitized != prompt:
            modified = True
            removed_items.append("PII")

        # -------------------------------------------------------
        # Step 2 : Remove placeholder fragments only
        # -------------------------------------------------------

        for placeholder in self.PII_PLACEHOLDERS:

            pattern = (
                r".*?"
                + re.escape(placeholder)
                + r".*?(?:\.|\n|$)"
            )

            new_text = re.sub(
                pattern,
                "",
                sanitized,
                flags=re.IGNORECASE,
            )

            if new_text != sanitized:
                sanitized = new_text

        # -------------------------------------------------------
        # Step 3 : Remove prompt injection phrases
        # -------------------------------------------------------

        for pattern in self.PROMPT_INJECTION_PATTERNS:

            new_text = re.sub(
                pattern,
                "",
                sanitized,
                flags=re.IGNORECASE,
            )

            if new_text != sanitized:

                sanitized = new_text

                modified = True

                if "Prompt Injection" not in removed_items:
                    removed_items.append("Prompt Injection")

        # -------------------------------------------------------
        # Step 4 : Remove role manipulation phrases
        # -------------------------------------------------------

        for pattern in self.ROLE_MANIPULATION_PATTERNS:

            new_text = re.sub(
                pattern,
                "",
                sanitized,
                flags=re.IGNORECASE,
            )

            if new_text != sanitized:

                sanitized = new_text

                modified = True

                if "Role Manipulation" not in removed_items:
                    removed_items.append("Role Manipulation")

        # -------------------------------------------------------
        # Step 5 : Remove leftover punctuation
        # -------------------------------------------------------

        sanitized = re.sub(r"\s+\.", ".", sanitized)
        sanitized = re.sub(r"\s+,", ",", sanitized)
        sanitized = re.sub(r"\s+!", "!", sanitized)
        sanitized = re.sub(r"\s+\?", "?", sanitized)

        # collapse repeated punctuation

        sanitized = re.sub(r"\.{2,}", ".", sanitized)

        # remove empty parentheses

        sanitized = re.sub(r"\(\s*\)", "", sanitized)

        # collapse spaces

        sanitized = re.sub(r"[ \t]+", " ", sanitized)

        # collapse blank lines

        sanitized = re.sub(r"\n\s*\n+", "\n", sanitized)

        # remove leading punctuation

        sanitized = re.sub(r"^[\s,.;:!-]+", "", sanitized)

        sanitized = sanitized.strip()

        # -------------------------------------------------------
        # Step 6 : Final result
        # -------------------------------------------------------

        return SanitizationResult(
            original_prompt=prompt,
            sanitized_prompt=sanitized,
            modified=modified,
            removed_items=removed_items,
            explanation=(
                "Prompt sanitized successfully."
                if modified
                else "Prompt did not require sanitization."
            ),
            confidence=1.0,
        )