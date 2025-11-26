import pytest
from unittest.mock import MagicMock, patch
from agents.data_analyst_agent import create_data_analyst_agent
from agents.forecasting_agent import create_forecasting_agent
from google.adk.models.base_llm import BaseLlm
from typing import Any

class MockModel(BaseLlm):
    def __init__(self, model: str = "mock-model"):
        super().__init__(model=model)
    
    def prompt(self, prompt: str, **kwargs) -> Any:
        return "Mock Response"

    async def generate_content_async(self, prompt: str, **kwargs) -> Any:
        return "Mock Response"

# Mock Gemini to avoid API calls during tests
@patch("agents.data_analyst_agent.Gemini", return_value=MockModel())
def test_data_analyst_initialization(mock_gemini):
    agent = create_data_analyst_agent()
    assert agent.name == "data_analyst"
    assert len(agent.tools) == 2

@patch("agents.forecasting_agent.Gemini", return_value=MockModel())
def test_forecaster_initialization(mock_gemini):
    agent = create_forecasting_agent()
    assert agent.name == "forecaster"
    assert len(agent.tools) == 1
