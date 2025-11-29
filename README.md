# Enterprise AI Analyst Agent (EDAMAS)

**EDAMAS** is a production-grade, multi-agent system built with the **Google Agent Development Kit (ADK)**. This application automatically profiles, cleans, analyzes, visualizes, and reports on any business dataset in seconds. It orchestrates a team of specialized AI agents to generate forecasts, detect anomalies, and produce executive-level reports.

## 🚀 Features

- **Multi-Agent Architecture**: Five specialized agents working in concert:
  - **Data Analyst**: Profiles and validates incoming datasets.
  - **Forecaster**: Predicts future trends using Exponential Smoothing (Holt-Winters).
  - **Anomaly Detector**: Identifies outliers using Isolation Forest.
  - **Strategist**: Synthesizes internal findings with external market context.
  - **Reporter**: Generates polished HTML executive reports.
- **Official ADK Integration**: Built using `agent.yaml`, `LlmAgent`, and standard ADK patterns.
- **Dynamic Data Loading**: Supports CSV/Excel file uploads via the Gemini Agent UI.
- **Robust Testing**: Comprehensive `pytest` suite for all tools and agents.
- **Production Ready**: Includes type hinting, error handling, and modular design.

## 📂 Project Structure

```
enterprise_agents(v3)/
├── agent.yaml              # Main ADK configuration
├── agent.py                # Root agent entry point
├── agents/                 # Specialized agent definitions
│   ├── data_analyst_agent.py
│   ├── forecasting_agent.py
│   ├── anomaly_agent.py
│   ├── strategy_agent.py
│   └── report_agent.py
├── tools/                  # Functional tools (MCP-style)
│   ├── data_loader_tool.py
│   ├── profiling_tool.py
│   ├── forecasting_tool.py
│   ├── anomaly_tool.py
│   ├── search_tool.py
│   └── reporting_tool.py
├── memory/                 # Session and long-term memory
├── utils/                  # Configuration and validation
├── tests/                  # Pytest suite
└── requirements.txt        # Dependencies
```

## 🛠️ Installation

1.  **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd Enterprise-Agents(v3)
    ```

2.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    - Create a `.env` file in the root directory:
      ```bash
      cp .env.example .env
      ```
    - Add your Google API Key:
      ```env
      GOOGLE_API_KEY=your_api_key_here
      MODEL_NAME=gemini-2.5-flash
      ```

## 🏃 Usage

### Run with ADK UI (Recommended)

The easiest way to interact with the agent is using the ADK web interface:

```bash
adk web .
```

Then open your browser to the provided URL (usually `http://localhost:3000`).

### Run via Command Line

You can also run the agent directly from the terminal (if a CLI entry point is configured):

```bash
python agent.py
```

## 🏗️ Architecture

The system follows a hierarchical multi-agent pattern:

1.  **Root Agent (`EnterpriseAnalyst`)**: Receives the user request and orchestrates the workflow.
2.  **Sub-Agents**:
    - **Data Analyst** loads the file and checks data quality.
    - **Forecaster** & **Anomaly Detector** run parallel analysis models.
    - **Strategist** looks for external context to explain findings.
    - **Reporter** compiles everything into `executive_report.html`.

## 📊 Capstone Notes

This project demonstrates advanced agentic patterns:

- **Tool Use**: Integration of `pandas`, `scikit-learn`, and `statsmodels` as agent tools.
- **Orchestration**: Complex hand-offs between agents.
- **Structured Output**: Agents communicate via structured JSON data, not just text.
- **Memory**: Session state management for context preservation.
