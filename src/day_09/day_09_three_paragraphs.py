import os
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are a writer.

Constraints:
- Write in the style of a 1920s newspaper reporter
- Return exactly 3 paragraphs
"""

USER_PROMPT = "Describe what prompt engineering is and why it matters."

def count_paragraphs(text: str) -> int:
    paragraphs = re.split(r"\n\s*\n", text.strip())
    return len([p for p in paragraphs if p.strip()])

def run():
    prompt = f"""{ SYSTEM_PROMPT }  Question: { USER_PROMPT }"""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    text = response.candidates[0].content.parts[0].text.strip()
    print(text)
    print()
    print(f"Paragraphs detected: {count_paragraphs(text)}")

if __name__ == "__main__":
    run()
