from google.adk.agents import LlmAgent
from tools.data_loader_tool import load_data
from tools.profiling_tool import profile_data
from utils.config import Config
from google.adk.models.google_llm import Gemini

def create_data_analyst_agent():
    model = Gemini(model=Config.MODEL_NAME)
    
    return LlmAgent(
        model=model,
        name="data_analyst",
        description="Loads and profiles data to understand its structure and quality.",
        instruction="""
        You are a Data Analyst.
        Your goal is to load datasets and provide a comprehensive profile.
        
        1. If the user provides a file path, use `load_data` to load it.
        2. Once loaded, use `profile_data` to understand the columns, types, and missing values.
        3. Summarize the findings clearly.
        
        Always return structured insights about the data quality.
        """,
        tools=[load_data, profile_data]
    )
