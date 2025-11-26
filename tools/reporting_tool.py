import jinja2
import json
from datetime import datetime

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Executive Report</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #2c3e50; }
        .section { margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
        .alert { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Executive AI Report</h1>
    <p>Date: {{ date }}</p>
    
    <div class="section">
        <h2>Executive Summary</h2>
        <p>{{ summary }}</p>
    </div>
    
    <div class="section">
        <h2>Data Insights</h2>
        <p>{{ data_insights }}</p>
    </div>
    
    <div class="section">
        <h2>Forecast</h2>
        <p>{{ forecast }}</p>
    </div>
    
    <div class="section">
        <h2>Anomalies</h2>
        <ul>
        {% for anomaly in anomalies %}
            <li class="alert">{{ anomaly }}</li>
        {% endfor %}
        </ul>
    </div>
    
    <div class="section">
        <h2>Strategic Recommendations</h2>
        <p>{{ strategy }}</p>
    </div>
</body>
</html>
"""

def generate_report(summary: str, data_insights: str, forecast: str, anomalies: list[str], strategy: str, output_path: str = "executive_report.html") -> str:
    """
    Generates an HTML report.
    
    Args:
        summary (str): Executive summary.
        data_insights (str): Data analysis summary.
        forecast (str): Forecast summary.
        anomalies (list[str]): List of anomalies.
        strategy (str): Strategic advice.
        output_path (str): Path to save the report.
        
    Returns:
        str: Status message.
    """
    try:
        data = {
            "summary": summary,
            "data_insights": data_insights,
            "forecast": forecast,
            "anomalies": anomalies,
            "strategy": strategy,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        
        env = jinja2.Environment(loader=jinja2.BaseLoader())
        template = env.from_string(TEMPLATE)
        html_content = template.render(**data)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        return f"Report generated at {output_path}"
    except Exception as e:
        return f"Error generating report: {str(e)}"
