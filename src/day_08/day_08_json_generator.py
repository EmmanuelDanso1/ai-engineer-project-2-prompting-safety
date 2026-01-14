import json
import sys
from dotenv import load_dotenv
from google import genai

from src.p2.config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE
from src.p2.json_utils import (
    BOOK_RECOMMENDATION_SCHEMA_KEYS,
    validate_exact_keys,
)

load_dotenv()

# Fail fast if API key missing
if not GEMINI_API_KEY:
    print("[error] GEMINI_API_KEY is not set in .env")
    sys.exit(1)

# Gemini client 
client = genai.Client(api_key=GEMINI_API_KEY)

# SYSTEM PROMPT (STRICT)
system_prompt = f"""
You are a JSON generator.

You MUST output a single valid JSON object with EXACTLY these keys:
{BOOK_RECOMMENDATION_SCHEMA_KEYS}

Rules:
- Do not include extra keys
- Do not omit any key
- All values must be strings
- Output ONLY the JSON object
- No markdown
- No commentary
"""

user_prompt = "Recommend a book about AI engineering."

# Model call 
response = client.models.generate_content(
    model=MODEL_NAME,
    contents=[
        {
            "role": "user",
            "parts": [
                {
                    "text": system_prompt + "\n\n" + user_prompt
                }
            ],
        }
    ],
    config={
        "temperature": TEMPERATURE,
        "response_mime_type": "application/json",
    },
)

raw_text = response.candidates[0].content.parts[0].text

# Parse JSON

try:
    obj = json.loads(raw_text)
except json.JSONDecodeError as e:
    raise RuntimeError(f"Invalid JSON returned:\n{raw_text}") from e


# Validate schema

validate_exact_keys(obj, required_keys=BOOK_RECOMMENDATION_SCHEMA_KEYS)


# Print final result

print(json.dumps(obj, indent=2, sort_keys=True))
