SUMMARY_SCHEMA_KEYS: tuple[str, ...] = ("title", "summary", "keywords")


def validate_summary_payload(obj: dict) -> None:
    """
    Validate summary payload against schema rules.

    Rules:
    - Exact keys must match SUMMARY_SCHEMA_KEYS
    - title and summary must be strings
    - keywords must be list[str] with length between 3 and 8
    """

    if not isinstance(obj, dict):
        raise ValueError("Payload must be a dictionary")

    if tuple(sorted(obj.keys())) != tuple(sorted(SUMMARY_SCHEMA_KEYS)):
        raise ValueError(
            f"Invalid keys. Expected {SUMMARY_SCHEMA_KEYS}, got {tuple(obj.keys())}"
        )

    if not isinstance(obj["title"], str):
        raise ValueError("title must be a string")

    if not isinstance(obj["summary"], str):
        raise ValueError("summary must be a string")

    keywords = obj["keywords"]

    if not isinstance(keywords, list):
        raise ValueError("keywords must be a list")

    if not (3 <= len(keywords) <= 8):
        raise ValueError("keywords must contain between 3 and 8 items")

    for k in keywords:
        if not isinstance(k, str):
            raise ValueError("keywords must be list[str]")