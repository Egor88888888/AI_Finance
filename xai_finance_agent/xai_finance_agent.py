import os
import gradio as gr
import google.generativeai as genai
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

# 🔐 Установите ваш ключ Google Gemini в переменную окружения `GOOGLE_API_KEY`
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY environment variable not set")
genai.configure(api_key=api_key)

# ✅ Обёртка для Gemini вместо xAI
class GeminiModel:
    def __init__(self, model="gemini-pro"):
        self.model = genai.GenerativeModel(model)

    def run(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text

    def get_content_as_string(self):
        return str(self.run)

# 📊 Финансовый агент
agent = Agent(
    name="xAI Finance Agent",
    model=GeminiModel(),  # ВАЖНО
    tools=[
        DuckDuckGoTools(),
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)
    ],
    instructions=[
        "Always use tables to display financial/numerical data. For text data use bullet points and small paragraphs."
    ],
    show_tool_calls=True,
    markdown=True,
)

# 🚀 Обработка запроса
def run_agent(query: str) -> str:
    response = agent.run(query)
    if hasattr(response, "get_content_as_string"):
        return response.get_content_as_string()
    return str(response)

# 🖥️ Интерфейс Gradio
if __name__ == "__main__":
    gr.Interface(
        fn=run_agent,
        inputs="text",
        outputs="text",
        title="xAI Finance Agent with Gemini"
    ).launch(share=True)
