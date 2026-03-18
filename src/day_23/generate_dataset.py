import json
from pathlib import Path
import random

OUTPUT_PATH = Path("data/fine_tuning/train_50.jsonl")

system_prompt = (
    'You convert informal meeting notes into a strict JSON object with this schema: '
    '{"title":"string","action_items":["string"],"owners":["string"],"due_dates":["string"]}. '
    'action_items, owners, due_dates must be the same length. '
    'due_dates must be YYYY-MM-DD or "" if unknown. Return only JSON.'
)

titles = [
    "Marketing Meeting",
    "Engineering Standup",
    "Product Sync",
    "Operations Meeting",
    "Sales Meeting",
    "Finance Check-in",
    "Strategy Meeting",
    "Customer Support Meeting",
    "HR Meeting",
    "Design Review"
]

actions = [
    "prepare report",
    "update documentation",
    "review backlog",
    "draft proposal",
    "fix login bug",
    "collect user feedback",
    "update roadmap",
    "analyze competitor pricing",
    "schedule interviews",
    "finalize budget"
]

owners = [
    "John",
    "Sarah",
    "Mike",
    "Lisa",
    "Alex",
    "Emma",
    "David",
    "Olivia",
    "Team",
    "Someone"
]

dates = [
    "2026-03-28",
    "2026-03-30",
    "2026-04-01",
    "2026-04-03",
    "2026-04-05",
    "2026-04-07",
    "2026-04-10",
    ""
]


def random_example():
    title = random.choice(titles)

    num_items = random.randint(1, 3)

    action_items = random.sample(actions, num_items)
    owner_items = [random.choice(owners) for _ in range(num_items)]
    due_items = [random.choice(dates) for _ in range(num_items)]

    notes_parts = []

    for a, o, d in zip(action_items, owner_items, due_items):
        if d:
            notes_parts.append(f"{o} will {a} by {d}.")
        else:
            notes_parts.append(f"{o} will {a} soon.")

    notes = " ".join(notes_parts)

    user_prompt = f"{title} today. {notes}"

    assistant_output = {
        "title": title,
        "action_items": action_items,
        "owners": owner_items,
        "due_dates": due_items
    }

    return {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": json.dumps(assistant_output)}
        ]
    }


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for _ in range(50):
            example = random_example()
            f.write(json.dumps(example) + "\n")

    print("Generated 50 dataset examples at:", OUTPUT_PATH)


if __name__ == "__main__":
    main()