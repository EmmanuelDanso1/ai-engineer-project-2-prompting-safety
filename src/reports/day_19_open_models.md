# Day 19: Open vs Closed Models Research and Hybrid Routing Design

## Part 1: Open-Source Models Overview

### Model 1: Llama 3 8B
- Model ID: meta-llama/Meta-Llama-3-8B-Instruct
- Size: 8 billion parameters
- License: Meta Llama 3 Community License
- Use notes:
  - Good balance between performance and cost
  - Can run on a single GPU (16GB VRAM)
  - Suitable for chatbots, assistants, and classification tasks

---

### Model 2: Mistral 7B Instruct
- Model ID: mistralai/Mistral-7B-Instruct-v0.2
- Size: 7 billion parameters
- License: Apache 2.0
- Use notes:
  - Fully open and commercially usable
  - Efficient and fast
  - Good for production deployments

---

### Model 3: Phi-3 Mini
- Model ID: microsoft/Phi-3-mini-4k-instruct
- Size: 3.8 billion parameters
- License: MIT License
- Use notes:
  - Extremely efficient
  - Can run on low-cost GPUs or CPUs
  - Best for lightweight assistants

---

## Part 2: Hybrid Routing Design

### Scenario
A production chatbot serving customers.

### Routing Tiers

**Tier 1: Open model (default)**
- Model: Mistral 7B
- Handles:
  - General questions
  - FAQs
  - Basic chatbot interactions

**Tier 2: Closed model (fallback)**
- Model: GPT-4o (or equivalent)
- Handles:
  - Complex reasoning
  - Critical business logic
  - Safety-sensitive tasks

---

### Routing Rule

Use open model if:

- Input length < 1000 tokens
- No sensitive content
- Confidence score high

Use closed model if:

- Complex reasoning required
- Safety classification uncertain
- High business importance

---

### Safety Rule

Always use closed model if:

- Moderation risk detected
- Financial or legal decisions involved
- Identity verification tasks

---

## Part 3: Cost Comparison

### Closed Model Pricing

Provider: OpenAI GPT-4o pricing page  
Pricing (as of 2025):

Input: $5.00 per 1M tokens  
Output: $15.00 per 1M tokens  

Source: https://openai.com/pricing

---

### Assumptions

Average input tokens per request = 500  
Average output tokens per request = 300  

Number of requests per day = 1,000  

---

### Cost Per Request

Input cost:

500 tokens = 0.0005M tokens

Cost = 0.0005 × $5.00  
Cost = $0.0025

Output cost:

300 tokens = 0.0003M tokens

Cost = 0.0003 × $15.00  
Cost = $0.0045

Total cost per request:

$0.0025 + $0.0045 = $0.007

---

### Daily Cost (Closed Model)

Requests/day = 1000

Daily cost:

1000 × $0.007 = $7.00/day

---

## Part 4: Self-Hosting Cost

Cloud Provider: AWS  
Instance: g5.xlarge (NVIDIA A10G GPU)  

Cost: $1.006 per hour  

Source: AWS EC2 pricing page

---

### Daily Cost (Self-Hosted)

Cost/hour = $1.006

Cost/day:

1.006 × 24 = $24.14/day

---

## Part 5: Break-Even Calculation

We find requests/day where API cost = self-host cost.

API cost per request = $0.007  
Self-host cost/day = $24.14

Break-even requests/day:

requests × 0.007 = 24.14

requests = 24.14 / 0.007

requests = 3448 requests/day

---

## Break-Even Result

Break-even point ≈ 3,448 requests per day

---

## Interpretation

If requests/day < 3,448:
Closed model API is cheaper

If requests/day > 3,448:
Self-hosting becomes cheaper

---

## Part 6: Final Recommendation

Best architecture: Hybrid system

Use open model for:

- Most requests
- Reduce costs

Use closed model for:

- Complex tasks
- Safety-critical tasks

Benefits:

- Lower cost
- Better safety
- Higher reliability
- Scalable architecture

---

## Conclusion

Closed models are cheaper at low scale.  
Open models become cheaper at high scale.  

Hybrid routing provides the best balance of:

- Cost
- Performance
- Safety
- Scalability
