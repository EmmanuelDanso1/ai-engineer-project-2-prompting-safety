import re

REDACTED = "[REDACTED_PII]"


def redact_pii(text: str) -> str:
    """
    Redact emails and phone numbers from text.
    """

    # Email regex
    email_pattern = re.compile(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    )

    # Phone number regex (supports many formats)
    phone_pattern = re.compile(
        r"""
        (\+?\d{1,3}[\s-]?)?          # country code
        (\(?\d{3}\)?[\s-]?)         # area code
        \d{3}[\s-]?\d{4}            # number
        """,
        re.VERBOSE,
    )

    # Replace emails
    text = email_pattern.sub(REDACTED, text)

    # Replace phones
    text = phone_pattern.sub(REDACTED, text)

    return text
