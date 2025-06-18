from agno.agent import Agent
from agno.models.xai import xAI
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import gradio as gr

agent = Agent(
    name="xAI Finance Agent",
    model=xAI(id="grok-beta"),
    tools=[DuckDuckGoTools(), YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Always use tables to display financial/numerical data. For text data use bullet points and small paragrpahs."],
    show_tool_calls=True,
    markdown=True,
)

def run_agent(query: str) -> str:
    """Run the xAI finance agent and return the response as a string."""
    response = agent.run(query)
    if hasattr(response, "get_content_as_string"):
        return response.get_content_as_string()
    return str(response)


if __name__ == "__main__":
    interface = gr.Interface(fn=run_agent, inputs="text", outputs="text", title="xAI Finance Agent")
    interface.launch(share=True)
