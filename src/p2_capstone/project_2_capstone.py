import json
import os

from src.p2.pii import redact_pii
from src.p2.moderation import moderate_text
from src.p2.prompt_utils import build_delimited_prompt
from src.p2.json_utils import validate_summary_payload

# example Gemini usage
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"


def call_llm(prompt: str) -> str:
    """
    Call Gemini with JSON forcing.
    """

    model = genai.GenerativeModel(MODEL_NAME)

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2,
            "response_mime_type": "application/json",
        },
    )

    return response.text


def summarize_securely(raw_text: str) -> dict:
    """
    Secure summarization pipeline.
    """

    # PII REDACTION
    redacted = redact_pii(raw_text)
    print("DEBUG INPUT:", redacted)

    # INPUT MODERATION
    if moderate_text(redacted):
        return {"title": "", "summary": "BLOCKED_INPUT", "keywords": []}


    # PROMPT CONSTRUCTION (DELIMITER + SANDWICH DEFENSE)

    instructions = """
You are a secure summarization assistant.

Return ONLY valid JSON using this schema:

{
"title": string,
"summary": string,
"keywords": [string]
}

Rules:
- keywords must contain between 3 and 8 items
- no extra fields
- output must be valid JSON
"""

    prompt = build_delimited_prompt(instructions, redacted)

    # LLM CALL
    output_text = call_llm(prompt)

    # OUTPUT MODERATION
    if moderate_text(output_text):
        return {"title": "", "summary": "BLOCKED_OUTPUT", "keywords": []}

    # PARSE + VALIDATE JSON
    try:
        obj = json.loads(output_text)
    except json.JSONDecodeError:
        raise ValueError("Model output was not valid JSON")

    validate_summary_payload(obj)

    return obj
    