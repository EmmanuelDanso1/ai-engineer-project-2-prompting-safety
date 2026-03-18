import json
from pathlib import Path


REQUIRED_KEYS = {"tasks"}
EXPECTED_TASK_KEYS = {"task", "owner", "due_date"}


def load_eval_dataset(eval_path):
    data = []
    with open(eval_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


import random

def mock_model_response(user_text, mode):
    """
    Simulate different quality outputs for each mode
    """

    if mode == "baseline":

        # 40% chance to produce bad output
        if random.random() < 0.4:
            return "Task: someone should do something"

    if mode == "prompt_engineered":

        # 15% chance to produce invalid JSON
        if random.random() < 0.15:
            return '{"task": "missing schema"}'

    # correct schema
    return '{"tasks":[{"task":"Example task","owner":"Someone","due_date":"Tomorrow"}]}'


def validate_schema(output):
    try:
        parsed = json.loads(output)
    except Exception:
        return False

    if set(parsed.keys()) != REQUIRED_KEYS:
        return False

    tasks = parsed["tasks"]

    if not isinstance(tasks, list):
        return False

    for t in tasks:
        if set(t.keys()) != EXPECTED_TASK_KEYS:
            return False

    return True


def schema_success_rate(*, model_name: str, eval_path: str, mode: str) -> float:

    if mode == "fine_tuned":
        print("fine_tuned: simulated")
        return -1.0

    dataset = load_eval_dataset(eval_path)

    successes = 0
    failures = []

    for item in dataset:

        user_prompt = item["messages"][1]["content"]

        if mode == "baseline":
            system_prompt = "Return JSON."

        elif mode == "prompt_engineered":
            system_prompt = (
                "Extract tasks from meeting notes and return JSON with key 'tasks'. "
                "Each task must include task, owner, due_date."
            )

        # simulate model
        output = mock_model_response(user_prompt, mode)
        if validate_schema(output):
            successes += 1
        else:
            failures.append(output)

    rate = successes / len(dataset)

    if mode == "baseline":
        print("\nFailure examples:")
        for f in failures[:2]:
            print(f)

    return rate


if __name__ == "__main__":

    eval_path = "data/fine_tuning/eval_20.jsonl"

    baseline = schema_success_rate(
        model_name="gpt-base",
        eval_path=eval_path,
        mode="baseline"
    )

    prompt_engineered = schema_success_rate(
        model_name="gpt-base",
        eval_path=eval_path,
        mode="prompt_engineered"
    )

    fine_tuned = schema_success_rate(
        model_name="ft-model",
        eval_path=eval_path,
        mode="fine_tuned"
    )

    print("\n=== RESULTS ===")
    print("Baseline:", baseline)
    print("Prompt Engineered:", prompt_engineered)
    print("Fine Tuned:", fine_tuned)