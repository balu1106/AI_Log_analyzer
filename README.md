# AI Log Analyzer

## Overview

AI Log Analyzer is a tool that helps developers analyze system logs and detect anomalies automatically using AI techniques.

## Problem Statement

Modern applications generate massive volumes of logs, making it difficult to manually identify issues, anomalies, or failures in real time.

## Solution

This project parses logs and applies intelligent techniques to detect anomalies and provide insights through a simple UI.

## Features

* Log parsing
* Anomaly detection
* Interactive UI using Streamlit
* Easy visualization of results

## Tech Stack

* Python
* Streamlit
* Machine Learning
* Regex-based parsing

## Installation

git clone https://github.com/balu1106/AI_Log_analyzer.git
cd AI_Log_analyzer
pip install -r requirements.txt

## Run

streamlit run app.py

## Challenges

* Handling multiple log formats
* Efficient anomaly detection
* Real-time responsiveness

## Future Improvements

* Real-time streaming logs
* Advanced ML models
* Alert system integration
  
## Methodology
- Logs are parsed using regex-based techniques
- Features are extracted from log patterns
- Anomaly detection is performed using basic statistical / ML techniques (e.g., thresholding / clustering)

## Output
- Highlights anomalous log entries
- Displays results using Streamlit UI
