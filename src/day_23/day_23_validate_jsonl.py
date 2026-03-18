import json
from pathlib import Path
from src.p2.tokens import count_text_tokens

DATASET_PATH = Path("data/fine_tuning/train_50.jsonl")
MODEL_NAME = "gpt-4o-mini"


def validate_dataset():

    if not DATASET_PATH.exists():
        raise FileNotFoundError(f"{DATASET_PATH} not found")

    lines = DATASET_PATH.read_text().strip().splitlines()

    if len(lines) != 50:
        raise ValueError(f"Dataset must contain exactly 50 lines. Found {len(lines)}")

    total_tokens = 0

    for i, line in enumerate(lines, start=1):

        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            raise ValueError(f"Line {i} is not valid JSON")

        if "messages" not in obj:
            raise ValueError(f"Line {i} missing messages")

        messages = obj["messages"]

        if len(messages) != 3:
            raise ValueError(f"Line {i} must have exactly 3 messages")

        roles = [m["role"] for m in messages]

        if roles != ["system", "user", "assistant"]:
            raise ValueError(f"Line {i} roles must be system,user,assistant")

        assistant_content = messages[2]["content"]

        try:
            assistant_json = json.loads(assistant_content)
        except json.JSONDecodeError:
            raise ValueError(f"Line {i} assistant content not valid JSON")

        required_keys = ["title", "action_items", "owners", "due_dates"]

        for key in required_keys:
            if key not in assistant_json:
                raise ValueError(f"Line {i} missing key {key}")

        action_items = assistant_json["action_items"]
        owners = assistant_json["owners"]
        due_dates = assistant_json["due_dates"]

        if not (len(action_items) == len(owners) == len(due_dates)):
            raise ValueError(f"Line {i} arrays must have same length")

        total_tokens += count_text_tokens(line, MODEL_NAME)

    print("PASS: validated 50 lines")
    print(f"Total tokens (estimated): {total_tokens}")


if __name__ == "__main__":
    validate_dataset()