# Day 24 — Fine-Tuning Workflow Explanation

A file ID is a unique identifier returned by the API after uploading a dataset used for fine-tuning. When a training dataset is uploaded, the system stores the file and assigns it a file ID so it can be referenced when creating a fine-tuning job. The file ID allows the training service to locate the dataset without needing to upload it again.

A job ID represents a specific fine-tuning process created by the system. Once a dataset file is uploaded, a fine-tuning job is started using that file ID. The API returns a job ID that can be used to track the training process. Each fine-tuning run has its own job ID because multiple training jobs may exist at the same time.

Polling is required because fine-tuning jobs take time to complete. Training a model involves processing many examples and adjusting model parameters, which can take minutes or hours depending on the dataset size. Polling allows the application to periodically check the job status until it finishes.

A custom model ID represents the final fine-tuned model produced by the training job. Once the job succeeds, the platform generates a unique identifier for the new model. This custom model ID can then be used for inference just like a normal model, but it reflects the behavior learned from the fine-tuning dataset.

Dry-run mode is used in this curriculum to demonstrate the workflow without requiring real API calls. It allows students to understand the sequence of steps in the fine-tuning pipeline while avoiding unnecessary costs or configuration issues. The script simulates file uploads, job creation, polling, and inference using mock IDs so that the workflow can be tested safely. This approach ensures the logic of the pipeline is correct before integrating with a real API.

- ## output 
Live mode: False
Dataset: data\fine_tuning\train_50.jsonl
=== STEP 1: UPLOAD FILE ===
(dry-run) mock file id: file_mock_123

=== STEP 2: CREATE JOB ===
(dry-run) mock job id: job_mock_123

=== STEP 3: POLL STATUS ===
status: running
status: running
status: running
status: succeeded
mock model id: ft:mock:model:abc123

=== STEP 4: INFERENCE WITH CUSTOM MODEL ID ===
Using model: ft:mock:model:abc123
Example API request payload:
{'model': 'ft:mock:model:abc123', 'messages': [{'role': 'user', 'content': 'Meeting notes: John should update the roadmap by next Friday.'}]}
Example response: Mock response from fine-tuned model
