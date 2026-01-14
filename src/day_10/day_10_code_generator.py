import json
import os
import importlib.util
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from src.p2.json_utils import validate_codegen_payload

# Setup

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=GEMINI_API_KEY)

USER_REQUEST = "Write a Python function to check if a string is a palindrome."

SYSTEM_PROMPT = """
You are a code generator.

You MUST return a single valid JSON object.
NO markdown.
NO explanations.
NO text outside the JSON.

The JSON MUST have this exact structure:

{
  "function_name": "string",
  "dependencies": ["string"],
  "description": "string",
  "code": "string"
}

Rules:
- Python 3.11+
- Include a docstring
- No external dependencies unless listed
- Do NOT use eval or exec
- Code must define exactly ONE function
"""



# Generation
def generate_code():
    full_prompt = f"""
{SYSTEM_PROMPT.strip()}

Question:
{USER_REQUEST}
""".strip()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=full_prompt,
    )

    raw_text = response.candidates[0].content.parts[0].text.strip()

    if not raw_text:
        raise RuntimeError("Model returned empty output")

    payload = json.loads(raw_text)
    validate_codegen_payload(payload)
    return payload

# Write + Test

def write_and_test(payload: dict):
    generated_dir = Path("generated/day_10")
    generated_dir.mkdir(parents=True, exist_ok=True)

    file_path = generated_dir / "palindrome.py"
    file_path.write_text(payload["code"], encoding="utf-8")

    # Dynamic import
    spec = importlib.util.spec_from_file_location(
        "palindrome", file_path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    func = getattr(module, payload["function_name"])

    assert func("racecar") is True
    assert func("hello") is False

    print("PASS: palindrome tests")

# Run

def main():
    payload = generate_code()
    write_and_test(payload)

if __name__ == "__main__":
    main()
