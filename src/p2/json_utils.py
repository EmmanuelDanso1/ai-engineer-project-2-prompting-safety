# BOOK_RECOMMENDATION_SCHEMA_KEYS: tuple[str, ...] = (
#     "title",
#     "author",
#     "genre",
#     "reasoning",
# )


# def validate_exact_keys(
#     obj: dict,
#     *,
#     required_keys: tuple[str, ...],
# ) -> None:
#     """
#     Validate that obj:
#     - is a dict
#     - contains exactly the required keys
#     - contains no extra keys
#     - all values are strings
#     """
#     if not isinstance(obj, dict):
#         raise ValueError("Output is not a JSON object")

#     obj_keys = set(obj.keys())
#     required = set(required_keys)

#     if obj_keys != required:
#         missing = required - obj_keys
#         extra = obj_keys - required
#         raise ValueError(
#             f"Invalid keys. Missing: {missing}, Extra: {extra}"
#         )

#     for key, value in obj.items():
#         if not isinstance(value, str):
#             raise ValueError(f"Value for '{key}' must be a string")

CODEGEN_SCHEMA_KEYS: tuple[str, ...] = (
    "function_name",
    "dependencies",
    "description",
    "code",
)

def validate_exact_keys(obj: dict, expected_keys: tuple[str, ...]) -> None:
    if set(obj.keys()) != set(expected_keys):
        raise ValueError(
            f"Invalid keys. Expected {expected_keys}, got {tuple(obj.keys())}"
        )

def validate_codegen_payload(obj: dict) -> None:
    validate_exact_keys(obj, CODEGEN_SCHEMA_KEYS)

    if not isinstance(obj["function_name"], str):
        raise TypeError("function_name must be a string")

    if not isinstance(obj["description"], str):
        raise TypeError("description must be a string")

    if not isinstance(obj["code"], str):
        raise TypeError("code must be a string")

    dependencies = obj["dependencies"]
    if not isinstance(dependencies, list):
        raise TypeError("dependencies must be a list")

    for dep in dependencies:
        if not isinstance(dep, str):
            raise TypeError("dependencies must be list[str]")
