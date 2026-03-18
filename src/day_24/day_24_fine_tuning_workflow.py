import os
import time
from pathlib import Path

DATASET_PATH = Path("data/fine_tuning/train_50.jsonl")

# mock model id used in dry-run
CUSTOM_MODEL_ID = "ft:mock:model:abc123"


def upload_file(dataset_path: Path, live_mode: bool):
    print("=== STEP 1: UPLOAD FILE ===")

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    if live_mode:
        # Placeholder for real API upload
        print("Uploading dataset to API...")
        file_id = "file_live_example"
    else:
        file_id = "file_mock_123"
        print(f"(dry-run) mock file id: {file_id}")

    return file_id


def create_fine_tune_job(file_id: str, live_mode: bool):
    print("\n=== STEP 2: CREATE JOB ===")

    if live_mode:
        print("Creating fine-tuning job using file:", file_id)
        job_id = "job_live_example"
    else:
        job_id = "job_mock_123"
        print(f"(dry-run) mock job id: {job_id}")

    return job_id


def poll_job_status(job_id: str, live_mode: bool):
    print("\n=== STEP 3: POLL STATUS ===")

    if live_mode:
        print("Polling real job status for:", job_id)
        status = "succeeded"
    else:
        for _ in range(3):
            print("status: running")
            time.sleep(1)

        status = "succeeded"
        print(f"status: {status}")
        print(f"mock model id: {CUSTOM_MODEL_ID}")

    return status


def run_inference(prompt: str):
    print("\n=== STEP 4: INFERENCE WITH CUSTOM MODEL ID ===")

    print("Using model:", CUSTOM_MODEL_ID)

    # Example inference function (not executed in dry-run)
    def call_model(user_prompt: str):
        """
        This function demonstrates how inference would work with the
        fine-tuned model ID.
        """

        request_payload = {
            "model": CUSTOM_MODEL_ID,
            "messages": [
                {"role": "user", "content": user_prompt}
            ]
        }

        # Example request payload
        print("Example API request payload:")
        print(request_payload)

        # In a real implementation, this would call the API
        # response = client.chat.completions.create(**request_payload)

        return "Mock response from fine-tuned model"

    response = call_model(prompt)
    print("Example response:", response)


def main():
    live_mode = os.getenv("P2_RUN_LIVE_FINE_TUNE") == "1"

    print("Live mode:", live_mode)
    print("Dataset:", DATASET_PATH)

    file_id = upload_file(DATASET_PATH, live_mode)
    job_id = create_fine_tune_job(file_id, live_mode)
    poll_job_status(job_id, live_mode)

    example_prompt = "Meeting notes: John should update the roadmap by next Friday."
    run_inference(example_prompt)


if __name__ == "__main__":
    main()