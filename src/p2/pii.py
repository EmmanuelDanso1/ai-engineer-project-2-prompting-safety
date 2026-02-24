import re
from typing import List

# Improved regex for phone and email
EMAIL_REGEX = re.compile(
    r'[\w\.-]+(\+[\w-]+)?@[\w\.-]+\.\w+', re.IGNORECASE
)
PHONE_REGEX = re.compile(
    r'(\+?\d[\d\s\.-]{7,}\d)', re.IGNORECASE
)

def redact_pii(text: str) -> str:
    text = EMAIL_REGEX.sub("[REDACTED_PII]", text)
    text = PHONE_REGEX.sub("[REDACTED_PII]", text)
    return text