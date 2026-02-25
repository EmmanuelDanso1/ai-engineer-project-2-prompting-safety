## Project 8 - Day 8: Understanding why structured output is essential for LLM integration into software.
Focus on ensuring the LLM's output is predictable and machine-readable, a necessity for integrating LLMs into any software pipeline. 

- ## The Necessity of Structured Output
Why structured output matters in production applications

- ## Forcing JSON Output via API
Forcing JSON Output via API

- ## Defining the Schema in the Prompt
How to define JSON schemas clearly in prompts

## Project 9 - Day 9: Day 9 continues structured output work by introducing output constraining beyond JSON: controlling length, format, and "no extra text" behaviors.
Apply max_tokens to constrain output length and control costs.
Design prompts that enforce strict formatting (single word, fixed paragraphs, no explanation).
Understand why grammar-based constraining exists and when prompt-only constraints fail.

- ## Length Control with max_tokens
How max_tokens controls output length
Best practices for setting max_tokens

- ## Prompt-Based Constraining 
Techniques for constraining content
Format constraints (single word, fixed paragraphs)

- ##  Grammar-Based Constraining
When prompt-only constraints fail
Comparison with prompt-based approaches

## Project 11 - Prompt injection security
The prompt-injection security block by teaching you what prompt injection is, why LLM applications need explicit defenses, and how to identify vulnerabilities.

- ## Objectives
Define prompt injection and distinguish direct vs. indirect injection.
Recognize common attacker goals (goal hijacking, data exfiltration, DoS).
Run simple injection tests against a vulnerable bot.

## Project 12 - Defensive prompting
Prompt structure patterns that make prompt injection harder (but not impossible). The core techniques are delimiters, explicit refusals, and the sandwich defense.

- ## Objectives
Use clear delimiters to isolate user content from instructions.
Implement the sandwich defense (reinforce instructions after user input).
Add a predictable refusal behavior for "instruction override" attempts.

## Project 13 -  Pre-LLM security layer
Input validation and sanitization. Defensive prompting helps, but want traditional software security checks before untrusted user input ever reaches the model.

- ## Objectives
Implement simple keyword-based blocking for common injection phrases.
Escape delimiter-breaking characters to prevent "tag closing" attacks.
Run an adversarial test cycle: attack → patch → re-test.

## Project 15 - Privacy and data leakage
Sending prompts to an LLM provider, you must assume user input could contain PII (Personally Identifiable Information). A basic mitigation is to detect and redact common PII patterns before any LLM call.
I update day 11 ask_bot to 15

- ## Objectives
Implementation of lightweight PII redaction (regex-based) for emails and phone numbers.
Integrating redaction into your request pipeline so raw input is never sent to the model.
Demonstrating why insecure code generation patterns (e.g., eval) are dangerous.

## Project 16 - Day 16 Introduces a dedicated Moderation API layer
Prompting and filters help, but policy classification should be handled by a specialized moderation model that can detect harmful content more reliably than prompt-based approaches.

- ## Objectives
Implement input moderation (block harmful user prompts before LLM call).
Implement output moderation (block harmful model outputs before display).
Design "graceful failure" messages when content is blocked.

## Project 17 - Day 17 introduces end-user identification in requests
 In production systems, linking requests to a non-PII user ID enables abuse monitoring, per-user rate limiting, and auditability.

- ## Objectives
Generate a non-PII user/session ID (UUID).
Pass that ID in the API request where supported (e.g., user= gemini API calls).
Document how user IDs support monitoring and compliance.

## Project 17 - Adversarial testing
Attempt to bypass moderation (obfuscation/evasion) and PII redaction (format edge cases), then patch weaknesses and re-test in a security hardening cycle.

- ## Objectives
Design evasion attempts for moderation and keyword filters.
Identify PII formats your redactor misses.
Patch and validate fixes with repeatable tests.

## Project 20 - Day 20 is hands-on open-source experimentation
Runnin a local model and compare latency/quality to a hosted closed model. This makes the "open vs closed" trade-offs concrete through practical experience.

- ## Objectives
Run a local inference server (recommended: Ollama).
Call a local model via an OpenAI-compatible base URL.
Measure and compare response latency and quality.