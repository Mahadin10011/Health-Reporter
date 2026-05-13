# System Health Reporter Agent

An agentic AI tool that monitors your system's health, detects issues, 
generates a plain-English diagnostic report, and sends a desktop alert 
— all running locally with no API keys required.

Built for the Operating Systems course project (4-week sprint).

## What it does

- Collects real-time CPU, memory, disk, and process metrics via psutil
- Flags issues based on configurable thresholds
- Generates a narrative health report using a local LLM (Ollama + Llama 3.2)
- Writes a timestamped Markdown report to disk
- Sends a desktop notification if critical issues are found

## Agentic behavior

The agent follows an observe → analyse → reason → act pipeline:
1. Observes OS metrics
2. Analyses against policy thresholds
3. Reasons about issues using a local LLM
4. Acts by writing a report and alerting the user

## Setup

### 1. Install Ollama
Download from https://ollama.com and install it, then run:
```bash
ollama pull llama3.2
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Run
```bash
python main.py
```

Reports are saved to the `reports/` folder as Markdown files.

## Project structure

```
health_reporter/
├── main.py          # pipeline orchestrator
├── collector.py     # OS metric collection (psutil)
├── analyser.py      # threshold-based flag detection
├── narrator.py      # LLM narrative generation (Ollama)
├── reporter.py      # Markdown report writer + notifications
├── config.json      # configurable thresholds
└── requirements.txt
```
