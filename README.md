# AI_Finance

This repository contains an implementation of the **xAI Finance Agent** example from [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps). The agent provides real-time financial analysis using Google's Gemini model, YFinance for stock data, and DuckDuckGo for web search. The code lives in [`xai_finance_agent/`](xai_finance_agent/).

## Quickstart
```bash
pip install -r xai_finance_agent/requirements.txt
export GOOGLE_API_KEY="<your API key>"
python xai_finance_agent/xai_finance_agent.py
```
This launches a Gradio chat interface with `share=True` so you can
interact with the agent in your browser.
