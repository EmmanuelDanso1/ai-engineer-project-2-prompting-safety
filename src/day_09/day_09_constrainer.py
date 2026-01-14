import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=GEMINI_API_KEY)

PROMPT = (
    'Summarize the Wikipedia entry for "Transformer (machine learning)" '
    "in plain English."
)

def run():
    # No max_tokens
    response_full = client.models.generate_content(
        model=MODEL_NAME,
        contents=PROMPT,
    )
    text_full = response_full.candidates[0].content.parts[0].text

    # max_tokens = 50
    response_short = client.models.generate_content(
        model=MODEL_NAME,
        contents=PROMPT,
        config={"max_output_tokens": 50},
    )
    text_short = response_short.text

    print("=== NO MAX TOKENS ===")
    print(text_full.strip())
    print()
    print("=== MAX_TOKENS=50 ===")
    print(text_short.strip())

if __name__ == "__main__":
    run()
