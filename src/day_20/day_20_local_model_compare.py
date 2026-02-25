import os
import time
from google import genai
from openai import OpenAI

PROMPT = "Write a 5-sentence summary of the Transformer architecture."

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Ollama local client
local_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


def run_remote():
    print("\n--- Remote Model (Gemini 2.5 Flash) ---")

    start = time.perf_counter()

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=PROMPT
    )

    end = time.perf_counter()

    print(response.text)
    print(f"elapsed_seconds={end - start:.3f}")


def run_local():
    print("\n--- Local Model (Ollama - mistral) ---")

    start = time.perf_counter()

    response = local_client.chat.completions.create(
        model="mistral",
        messages=[
            {"role": "user", "content": PROMPT}
        ],
        temperature=0
    )

    end = time.perf_counter()

    print(response.choices[0].message.content)
    print(f"elapsed_seconds={end - start:.3f}")


if __name__ == "__main__":
    run_remote()
    run_local()