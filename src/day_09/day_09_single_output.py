import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
Answer the question with ONLY the city name.

Rules:
- Output must be only the city name
- No punctuation
- No explanation
- No leading or trailing whitespace
"""

USER_PROMPT = "What is the capital of Ghana?"

def run():
    prompt = f"""
{SYSTEM_PROMPT}

Question:
{USER_PROMPT}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    text = response.candidates[0].content.parts[0].text.strip()
    print(text)

    if text != "Ottawa":
        raise ValueError("Output constraint failed: expected Ottawa")

if __name__ == "__main__":
    run()
