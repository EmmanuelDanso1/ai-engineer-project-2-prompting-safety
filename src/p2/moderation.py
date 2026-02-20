from dataclasses import dataclass
from typing import List

from google import genai
from google.genai.types import GenerateContentConfig

# Initialize Gemini client
client = genai.Client()

MODERATION_MODEL = "gemini-2.5-flash"


@dataclass
class ModerationResult:
    flagged: bool
    categories: List[str]


def moderate_text(text: str) -> ModerationResult:
    """
    Uses Gemini safety ratings to determine if text should be flagged.
    """

    response = client.models.generate_content(
        model=MODERATION_MODEL,
        contents=text,
        config=GenerateContentConfig(
            temperature=0
        )
    )

    flagged = False
    categories = []

    # Safety ratings exist inside candidates
    if response.candidates:
        safety_ratings = response.candidates[0].safety_ratings or []

        for rating in safety_ratings:

            category = rating.category.name
            probability = rating.probability.name

            # Flag MEDIUM or HIGH
            if probability in ["MEDIUM", "HIGH"]:
                flagged = True
                categories.append(category)

    return ModerationResult(
        flagged=flagged,
        categories=categories
    )