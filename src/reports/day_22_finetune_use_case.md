# Fine-Tuning Use Case: Meeting Notes to Structured JSON

This project uses fine-tuning to convert informal meeting notes into a strict JSON structure containing a meeting title, action items, owners, and due dates. While prompting alone can sometimes produce structured outputs, it is brittle because the model may generate additional text, reorder fields, or produce inconsistent JSON formatting. Fine-tuning allows the model to learn a consistent transformation pattern from unstructured notes into the required schema.

Success for this system would be measured by evaluating whether the output JSON is valid and whether the fields are extracted correctly. Metrics could include JSON validity rate, schema compliance rate, and extraction accuracy for action items, owners, and due dates. For example, a successful model might produce valid JSON in more than 98% of cases.

There are several risks in this approach. Overfitting could occur if the training dataset is too small or contains repetitive structures. Data quality is also critical; incorrect labels would teach the model incorrect mappings. Another potential risk is data leakage if confidential meeting notes were used in training.

Retrieval-Augmented Generation (RAG) would not solve this problem effectively because the task is not about retrieving external knowledge. Instead, it requires a deterministic transformation from informal text into a structured schema. Fine-tuning is therefore a better solution because it directly trains the model to perform this structured extraction task consistently.