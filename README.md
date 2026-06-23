# LLM Evaluation Platform V2

A Streamlit-based application designed to evaluate Large Language Model (LLM) responses using Google's Gemini API. The platform helps assess response quality, identify hallucinations, perform root cause analysis, and generate actionable recommendations through an interactive dashboard.

---

## Project Overview

As organizations increasingly adopt Generative AI solutions, ensuring response quality and factual accuracy has become critical. This project provides a framework for evaluating AI-generated responses against reference answers and identifying potential quality issues.

The platform leverages Gemini as an evaluation engine to score responses across multiple dimensions and present insights through an easy-to-use dashboard.

---

## Key Features

* Automated evaluation of AI-generated responses
* Relevance, completeness, and truthfulness scoring
* Hallucination detection
* Safety assessment
* Root Cause Analysis (RCA)
* Recommendation generation
* Interactive dashboard for analysis
* CSV export functionality
* Category-wise performance analysis

---

## Technology Stack

* Python
* Streamlit
* Pandas
* Google Gemini API
* TruthfulQA Dataset
* Python Dotenv

---

## Workflow

```text
Dataset Input
     ↓
Response Evaluation
     ↓
Gemini-Based Assessment
     ↓
Quality Scoring
     ↓
Root Cause Analysis
     ↓
Recommendations
     ↓
Dashboard Visualization
```

---

## Dashboard Capabilities

The platform provides visibility into:

* Overall response quality
* Truthfulness trends
* Hallucination levels
* Root cause distribution
* Recommendation analysis
* Category-level performance metrics

---

## Screenshots

### Dashboard Overview

![Dashboard](dashboard.png)

### Root Cause Analysis

![Root Cause Analysis](rca_analysis.png)

### Recommendation Analysis

![Recommendation Analysis](recommendation_analysis.png)

---

## Evaluation Metrics

Each response is evaluated across the following dimensions:

| Metric        | Description                                |
| ------------- | ------------------------------------------ |
| Relevance     | How well the response answers the question |
| Completeness  | Coverage of required information           |
| Truthfulness  | Factual accuracy of the response           |
| Hallucination | Presence of unsupported information        |
| Safety        | Safety and appropriateness of the response |
| Quality Score | Overall evaluation score                   |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Harikrishnan006/LLM-Evaluation-Platform-V2.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## Use Cases

* AI Response Quality Monitoring
* Hallucination Detection
* LLM Benchmarking
* AI Governance Initiatives
* Response Validation Workflows
* Internal AI Evaluation Frameworks

---

## Future Improvements

* Multi-model comparison
* Batch evaluation support
* API integration
* RAG evaluation workflows
* Advanced reporting and analytics

---

## Author

**Harikrishnan V**

AI Automation Associate | Former Amazon ML Data Associate

Focused on AI Operations, LLM Evaluation, Data Quality, and Process Automation.
