import sys
import os

# Add current directory to sys.path to ensure modules can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from utils.config import Config
from agents.data_analyst_agent import create_data_analyst_agent
from agents.forecasting_agent import create_forecasting_agent
from agents.anomaly_agent import create_anomaly_agent
from agents.strategy_agent import create_strategy_agent
from agents.report_agent import create_report_agent

def create_enterprise_analyst_agent():
    """
    Creates the root Enterprise Analyst Agent.
    """
    # Initialize sub-agents
    data_analyst = create_data_analyst_agent()
    forecaster = create_forecasting_agent()
    anomaly_detector = create_anomaly_agent()
    strategist = create_strategy_agent()
    reporter = create_report_agent()

    # Initialize root model
    model = Gemini(model=Config.MODEL_NAME)

    # Define the root agent
    agent = LlmAgent(
        model=model,
        name="EnterpriseAnalyst",
        description="Root agent that orchestrates the data analysis workflow.",
        instruction="""
        You are the Enterprise Analyst, a sophisticated multi-agent system.
        Your goal is to help users analyze their business data.
        
        You have access to a team of specialized agents:
        - Data Analyst: Profiles and understands data structure.
        - Forecaster: Predicts future trends.
        - Anomaly Detector: Identifies outliers.
        - Strategist: Provides strategic context.
        - Reporter: Generates final reports.
        
        Workflow:
        1.  Always start by understanding the user's request.
        2.  If data is needed, ask the user to upload it or use the data loader.
        3.  Delegate tasks to the appropriate sub-agents in a logical order.
            - Example: Profile -> Forecast -> Anomaly -> Strategy -> Report.
        4.  Maintain context between steps.
        
        Always be professional, concise, and helpful.
        """,
        sub_agents=[
            data_analyst,
            forecaster,
            anomaly_detector,
            strategist,
            reporter
        ]
    )
    
    return agent

# Instantiate the agent globally for ADK to pick up
root_agent = create_enterprise_analyst_agent()

if __name__ == "__main__":
    print(f"Agent {root_agent.name} initialized.")
