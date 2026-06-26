# LLM Evaluation Platform

> Evaluate LLM response quality using AI — score truthfulness, detect hallucinations, and generate improvement recommendations.

🔗 **Live Demo:** [Click to try the app](https://huggingface.co/spaces/Harikrishnan006/llm-evaluation-platform-v2)  
📁 **Type:** Portfolio Project — AI Engineering  
🛠 **Stack:** Python · Streamlit · Google Gemini · TruthfulQA · Hugging Face

---

![App Screenshot](screenshot.png)

---

## The Problem

As LLMs are adopted in production, response quality becomes critical. How do you know if your model is hallucinating? How do you measure truthfulness at scale? Manual review doesn't work beyond a handful of responses.

## The Solution

An automated evaluation platform that uses **Gemini as an AI judge** — scoring LLM responses across multiple quality dimensions and surfacing root causes and recommendations.

---

## How It Works

```
Load TruthfulQA Dataset
        ↓
Select sample size → Click Run Evaluation
        ↓
Each response sent to Gemini with evaluation prompt
        ↓
Gemini scores across 5 dimensions
        ↓
Quality Score · Root Cause · Recommendation generated
        ↓
Results table · Charts · CSV export
```

---

## Evaluation Metrics

| Metric | Description |
|---|---|
| Relevance | How well the response answers the question |
| Completeness | Coverage of required information |
| Truthfulness | Factual accuracy of the response |
| Hallucination | Presence of unsupported information (higher = worse) |
| Safety | Appropriateness of the response |
| Quality Score | Weighted composite of all metrics |

---

## Features

- Configure sample size and run evaluations on demand
- Per-response scoring across 5 quality dimensions
- Root Cause Analysis with distribution charts
- Recommendation generation for each response
- Category-level performance breakdown
- CSV export of all results
- Uses TruthfulQA — a standard LLM benchmarking dataset

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| UI | Streamlit |
| Evaluator LLM | Google Gemini 2.5 Flash |
| Dataset | TruthfulQA (Hugging Face Datasets) |
| Deployment | Hugging Face Spaces |

---

## Run Locally

```bash
git clone https://github.com/Harikrishnan006/LLM-Evaluation-Platform-V2.git
cd LLM-Evaluation-Platform-V2
pip install -r requirements.txt
echo "GEMINI_API_KEY=your_key_here" > .env
streamlit run app.py
```

Get a free Gemini API key at [aistudio.google.com](https://aistudio.google.com)

---

## Author

**Harikrishnan Venkatesan**  
AI Automation Associate · Vendasta  
Former ML Data Associate · Amazon (Rufus, Alexa+)

[LinkedIn](https://www.linkedin.com/in/harikrishnan-venkatesan) · [GitHub](https://github.com/Harikrishnan006) · [Hugging Face](https://huggingface.co/Harikrishnan006)
