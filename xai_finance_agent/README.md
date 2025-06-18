## 📊 AI Finance Agent with xAI Grok
This application creates a financial analysis agent powered by xAI's Grok model, combining real-time stock data with web search capabilities. It provides structured financial insights through a simple Gradio chat interface.

### Features
- Powered by xAI's Grok-beta model
- Real-time stock data analysis via YFinance
- Web search capabilities through DuckDuckGo
- Formatted output with tables for financial data
- Interactive Gradio interface

### How to get Started?
1. Clone the GitHub repository
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/ai_agent_tutorials/xai_finance_agent
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Get your xAI API Key and export it as an environment variable:
```bash
export XAI_API_KEY='your-api-key-here'
```
4. Run the agent to launch a Gradio interface:
```bash
python xai_finance_agent.py
```
