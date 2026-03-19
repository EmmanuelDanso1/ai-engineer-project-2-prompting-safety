import json

from src.p2_capstone.project_2_capstone import summarize_securely


SAMPLE_TEXT = """
Artificial intelligence is rapidly transforming software development.
Developers are using AI tools to write code faster, automate testing,
and improve productivity across engineering teams.
"""

def main():
    result = summarize_securely(SAMPLE_TEXT)

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()