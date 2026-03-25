import streamlit as st
import pandas as pd
from analyzer.parser import parse_logs
from analyzer.detector import detect
from analyzer.risk_engine import calculate_risk
from analyzer.insights import generate_insights

st.set_page_config(page_title="AI Secure Log Analyzer", layout="wide")

st.title("AI Secure Log Analyzer")

# Input section
uploaded_file = st.file_uploader("Upload log file", type=["log", "txt"])
text_input = st.text_area("Or paste log content")

content = ""

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

elif text_input:
    content = text_input

# Analyze button
if st.button("Analyze"):
    if content:
        lines = parse_logs(content)
        findings = detect(lines)
        score, level = calculate_risk(findings)
        insights = generate_insights(findings)

        # Risk Analysis
        st.subheader("Risk Analysis")

        if level == "high":
            st.error(f"Risk Level: {level.upper()} (Score: {score})")
        elif level == "medium":
            st.warning(f"Risk Level: {level.upper()} (Score: {score})")
        else:
            st.success(f"Risk Level: {level.upper()} (Score: {score})")

        # Summary
        st.subheader("Summary")
        if findings:
            st.write("Log contains sensitive data and potential security risks.")
        else:
            st.write("Log appears safe with no major risks detected.")

        # Findings Table
        st.subheader("Findings")
        if findings:
            df = pd.DataFrame(findings)
            st.dataframe(df)
        else:
            st.success("No issues found")

        # Insights
        st.subheader("Insights")
        for i in insights:
            st.write("- " + i)

        # Highlighted Logs
        st.subheader("Log Preview with Highlights")

        for i, line in enumerate(lines):
            risky = any(f["line"] == i + 1 for f in findings)

            if risky:
                st.markdown(
                    f"<span style='color:red'>Line {i+1}: {line}</span>",
                    unsafe_allow_html=True
                )
            else:
                st.write(f"Line {i+1}: {line}")

    else:
        st.error("Please upload or enter log data")