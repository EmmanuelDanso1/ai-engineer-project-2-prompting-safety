# Day 25 Evaluation Report

## Results

| Approach | Success Rate |
|--------|--------|
| Base model (baseline prompt) | 60% |
| Base model (prompt engineered) | 85% |
| Fine-tuned model | 95% |

## Interpretation

The evaluation compares three approaches for extracting structured tasks from meeting notes. The baseline model using a minimal prompt performed the worst, achieving approximately 60% schema success rate. In many cases the output either failed to produce valid JSON or did not follow the expected schema. This demonstrates that large language models do not always reliably follow strict formatting instructions when prompts are vague.

Prompt engineering significantly improved performance. By explicitly defining the schema and required fields in the system prompt, the success rate increased to about 85%. This improvement shows that carefully structured prompts can guide the model toward more consistent outputs.

However, prompt engineering still leaves some edge cases where the schema may be violated. Fine-tuning addresses this by training the model directly on structured examples. With fine-tuning, the success rate increases to approximately 95%, producing more reliable JSON outputs.

Fine-tuning becomes worthwhile when applications require strict structured outputs, such as automated pipelines, data extraction systems, or integrations with downstream APIs. While prompt engineering is often sufficient for many tasks, fine-tuning is valuable when reliability and schema consistency are critical.

Overall, this experiment demonstrates the progressive improvements gained from baseline prompting to prompt engineering and finally to fine-tuning.