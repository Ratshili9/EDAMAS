from google.adk.agents import LlmAgent
from tools.reporting_tool import generate_report
from utils.config import Config
from google.adk.models.google_llm import Gemini

def create_report_agent():
    model = Gemini(model=Config.MODEL_NAME)
    
    return LlmAgent(
        model=model,
        name="reporter",
        description="Generates a final executive report.",
        instruction="""
        You are an Executive Reporter.
        Your goal is to compile all findings into a polished HTML report.
        
        1. Gather all insights from the conversation history (Data, Forecast, Anomalies, Strategy).
        2. Use `generate_report` to create the file.
        3. Ensure the summary is concise and the recommendations are clear.
        4. Confirm to the user when the report is ready and provide the path.
        """,
        tools=[generate_report]
    )
