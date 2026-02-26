# Day 21 – Hugging Face Models

## Text Classification Model

Model ID: distilbert-base-uncased-finetuned-sst-2-english  
Parameter Size: ~66M  
License: Apache-2.0  

Intended Use:
This model is fine-tuned on the SST-2 dataset for binary sentiment classification (positive/negative). It is lightweight and runs efficiently on CPU, making it suitable for local experimentation and production prototypes.

---

## Summarization Model

Model ID: sshleifer/distilbart-cnn-12-6  
Parameter Size: ~306M  
License: Apache-2.0  

Intended Use:
This model is a distilled version of BART fine-tuned on the CNN/DailyMail dataset for abstractive summarization. It provides good summarization quality while remaining efficient enough to run on CPU.