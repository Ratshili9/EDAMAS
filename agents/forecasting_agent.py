from google.adk.agents import LlmAgent
from tools.forecasting_tool import generate_forecast
from utils.config import Config
from google.adk.models.google_llm import Gemini

def create_forecasting_agent():
    model = Gemini(model=Config.MODEL_NAME)
    
    return LlmAgent(
        model=model,
        name="forecaster",
        description="Predicts future trends using statistical models.",
        instruction="""
        You are a Forecaster.
        Your goal is to predict future values based on historical data.
        
        1. Identify the date column and the value column from the data context.
        2. Use `generate_forecast` to predict future trends.
        3. Explain the forecast trend (upward, downward, stable).
        
        If you don't know which columns to use, ask for clarification or infer from the data profile.
        """,
        tools=[generate_forecast]
    )
