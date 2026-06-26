LLM Evaluation Platform


Evaluate LLM response quality using AI — score truthfulness, detect hallucinations, and generate improvement recommendations.



🔗 Live Demo: Click to try the app

📁 Type: Portfolio Project — AI Engineering

🛠 Stack: Python · Streamlit · Google Gemini · TruthfulQA · Pandas · Hugging Face


Show Image


The Problem

As LLMs are adopted in production, response quality becomes critical. How do you know if your model is hallucinating? How do you measure truthfulness at scale? Manual review doesn't work beyond a handful of responses.

The Solution

An automated evaluation platform that uses Gemini as an AI judge — scoring LLM responses across multiple quality dimensions and surfacing root causes and recommendations.


How It Works

Load TruthfulQA Dataset
        ↓
Select sample size → Click Run Evaluation
        ↓
Each response sent to Gemini with evaluation prompt
        ↓
Gemini scores: Relevance · Completeness · Truthfulness · Hallucination · Safety
        ↓
Quality Score computed · Root Cause identified · Recommendation generated
        ↓
Results table · Charts · CSV export


Evaluation Metrics

MetricDescriptionRelevanceHow well the response answers the questionCompletenessCoverage of required informationTruthfulnessFactual accuracy of the responseHallucinationPresence of unsupported information (higher = worse)SafetyAppropriateness of the responseQuality ScoreWeighted composite of all metrics


Features


Configure sample size and run evaluations on demand
Per-response scoring across 5 dimensions
Root Cause Analysis with distribution charts
Recommendation generation for each response
Category-level performance breakdown
CSV export of all results
Uses TruthfulQA — a standard LLM benchmarking dataset



Tech Stack

LanguagePython 3.10+UIStreamlitEvaluator LLMGoogle Gemini 2.5 FlashDatasetTruthfulQA (via Hugging Face Datasets)DeploymentHugging Face Spaces


Run Locally

bashgit clone https://github.com/Harikrishnan006/LLM-Evaluation-Platform-V2.git
cd LLM-Evaluation-Platform-V2
pip install -r requirements.txt
# Add GEMINI_API_KEY to .env
streamlit run app.py

Get a free Gemini API key at aistudio.google.com


Author

Harikrishnan Venkatesan

AI Automation Associate · Vendasta

Former ML Data Associate · Amazon (Rufus, Alexa+)

LinkedIn · GitHub · Hugging Face
