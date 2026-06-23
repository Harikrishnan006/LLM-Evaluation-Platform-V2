import streamlit as st
import pandas as pd

from evaluator import evaluate_response

st.set_page_config(
    page_title="LLM Evaluation Platform",
    layout="wide"
)

st.title("LLM Response Quality & Hallucination Detection Platform")

# Load Dataset
df = pd.read_parquet("truthfulqa.parquet")

results = []

# Demo Mode: Evaluate only 1 record to avoid API quota issues
for _, row in df.head(1).iterrows():

    evaluation = evaluate_response(
        row["question"],
        row["best_answer"],
        row["correct_answers"],
        row["incorrect_answers"]
    )

    results.append(evaluation)

evaluation_df = pd.DataFrame(results)

final_df = pd.concat(
    [df, evaluation_df],
    axis=1
)

# Evaluation Results
st.subheader("Evaluation Results")

st.dataframe(
    final_df.head(50),
    use_container_width=True
)

# Dashboard
st.subheader("Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Records",
        len(final_df)
    )

with col2:
    st.metric(
        "Avg Relevance",
        round(final_df["relevance"].mean(), 2)
    )

with col3:
    st.metric(
        "Avg Truthfulness",
        round(final_df["truthfulness"].mean(), 2)
    )

with col4:
    st.metric(
        "Avg Hallucination",
        round(final_df["hallucination"].mean(), 2)
    )

with col5:
    st.metric(
        "Avg Quality",
        round(final_df["quality_score"].mean(), 2)
    )

hallucination_count = (
    final_df["hallucination"] >= 7
).sum()

st.metric(
    "High Hallucination Responses",
    int(hallucination_count)
)

# Download Results
st.download_button(
    label="Download Results CSV",
    data=final_df.to_csv(index=False),
    file_name="evaluation_results.csv",
    mime="text/csv"
)

# Root Cause Analysis
st.subheader("Root Cause Analysis")

root_cause_counts = (
    final_df["root_cause"]
    .value_counts()
)

st.dataframe(
    root_cause_counts.reset_index(),
    use_container_width=True
)

# Recommendation Analysis
st.subheader("Recommendation Analysis")

recommendation_counts = (
    final_df["recommendation"]
    .value_counts()
)

st.dataframe(
    recommendation_counts.reset_index(),
    use_container_width=True
)

# Root Cause Distribution
st.subheader("Root Cause Distribution")

st.bar_chart(
    final_df["root_cause"].value_counts()
)

# Recommendation Distribution
st.subheader("Recommendation Distribution")

st.bar_chart(
    final_df["recommendation"].value_counts()
)

# Category Analysis
st.subheader("Category Analysis")

category_metrics = (
    final_df.groupby("category")
    [["truthfulness", "hallucination"]]
    .mean()
)

st.dataframe(
    category_metrics,
    use_container_width=True
)
