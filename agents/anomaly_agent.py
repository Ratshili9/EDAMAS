from google.adk.agents import LlmAgent
from tools.anomaly_tool import detect_anomalies
from utils.config import Config
from google.adk.models.google_llm import Gemini

def create_anomaly_agent():
    model = Gemini(model=Config.MODEL_NAME)
    
    return LlmAgent(
        model=model,
        name="anomaly_detector",
        description="Identifies outliers and anomalies in the data.",
        instruction="""
        You are an Anomaly Detector.
        Your goal is to find data points that deviate significantly from the norm.
        
        1. Identify the numerical column to check.
        2. Use `detect_anomalies` to find outliers.
        3. Report the number of anomalies and list the most significant ones.
        4. Assess the risk level based on the anomalies found.
        """,
        tools=[detect_anomalies]
    )
