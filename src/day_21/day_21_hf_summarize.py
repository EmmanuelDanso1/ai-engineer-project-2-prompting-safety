from transformers import pipeline

MODEL_ID = "sshleifer/distilbart-cnn-12-6"

MAX_LENGTH = 60

TEXT = """
Large Language Models (LLMs) are built on the Transformer architecture. 
They learn statistical patterns from large text corpora and can generate coherent text in response to prompts. 
In practical applications, engineers must handle token limits, prompt injection risks, and safety constraints. 
Production systems often combine multiple layers: input validation, moderation, and structured output parsing.
"""

def main():
    summarizer = pipeline(
        "summarization",
        model=MODEL_ID
    )

    summary = summarizer(
        TEXT,
        max_length=MAX_LENGTH,
        min_length=20,
        do_sample=False
    )[0]["generated_text"]

    print("Summary:")
    print(summary)
    print("\nMax Length Used:", MAX_LENGTH)


if __name__ == "__main__":
    main()