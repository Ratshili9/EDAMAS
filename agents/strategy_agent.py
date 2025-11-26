from google.adk.agents import LlmAgent
from tools.search_tool import search_market_context
from utils.config import Config
from google.adk.models.google_llm import Gemini

def create_strategy_agent():
    model = Gemini(model=Config.MODEL_NAME)
    
    return LlmAgent(
        model=model,
        name="strategist",
        description="Provides strategic advice based on internal data and external market context.",
        instruction="""
        You are a Business Strategist.
        Your goal is to synthesize internal data findings with external market context.
        
        1. Review the insights provided by the Data Analyst, Forecaster, and Anomaly Detector.
        2. Use `search_market_context` to find relevant external trends (e.g., "retail trends 2024", "supply chain issues").
        3. Combine internal and external insights to provide actionable strategic recommendations.
        """,
        tools=[search_market_context]
    )
