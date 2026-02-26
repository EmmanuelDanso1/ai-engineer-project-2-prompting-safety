import json
from transformers import pipeline

# Model ID constant
MODEL_ID = "distilbert-base-uncased-finetuned-sst-2-english"

def main():
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model=MODEL_ID
    )

    inputs = [
        "I love this course.",
        "This was a terrible experience.",
        "It was fine, nothing special."
    ]

    for text in inputs:
        result = sentiment_pipeline(text)[0]

        output = {
            "input": text,
            "label": result["label"],
            "score": result["score"]
        }

        print(json.dumps(output))


if __name__ == "__main__":
    main()