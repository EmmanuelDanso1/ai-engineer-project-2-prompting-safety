BOOK_RECOMMENDATION_SCHEMA_KEYS: tuple[str, ...] = (
    "title",
    "author",
    "genre",
    "reasoning",
)


def validate_exact_keys(
    obj: dict,
    *,
    required_keys: tuple[str, ...],
) -> None:
    """
    Validate that obj:
    - is a dict
    - contains exactly the required keys
    - contains no extra keys
    - all values are strings
    """
    if not isinstance(obj, dict):
        raise ValueError("Output is not a JSON object")

    obj_keys = set(obj.keys())
    required = set(required_keys)

    if obj_keys != required:
        missing = required - obj_keys
        extra = obj_keys - required
        raise ValueError(
            f"Invalid keys. Missing: {missing}, Extra: {extra}"
        )

    for key, value in obj.items():
        if not isinstance(value, str):
            raise ValueError(f"Value for '{key}' must be a string")
