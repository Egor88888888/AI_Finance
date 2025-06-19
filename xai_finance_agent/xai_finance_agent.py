import os
import gradio as gr
import google.generativeai as genai
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

# Установка API ключа
os.environ["GOOGLE_API_KEY"] = "AIzaSyD-oRb45v1ZuBy9MS4Ho-L-7BiU21qSsAE"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Класс обёртка для Gemini (вместо xAI)
class GeminiModel:
    def __init__(self, model="gemini-pro"):
        self.model = genai.GenerativeModel(model)

    def run(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text

    def get_content_as_string(self):
        return str(self.run)

# Инициализация агента
agent = Agent(
    name="xAI Finance Agent",
    model=GeminiModel(),  # заменили xAI
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

# Обработка запроса
def run_agent(query: str) -> str:
    response = agent.run(query)
    if hasattr(response, "get_content_as_string"):
        return response.get_content_as_string()
    return str(response)

# Интерфейс Gradio
if __name__ == "__main__":
    gr.Interface(fn=run_agent, inputs="text", outputs="text", title="xAI Finance Agent with Gemini").launch(share=True)
