import pytest
import json
from tools.data_loader_tool import load_data
from tools.profiling_tool import profile_data
from tools.forecasting_tool import generate_forecast
from tools.anomaly_tool import detect_anomalies
from tools.reporting_tool import generate_report

# Mock data creation for tests
@pytest.fixture
def sample_csv(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    p = d / "test_data.csv"
    p.write_text("date,value\n2023-01-01,100\n2023-01-02,110\n2023-01-03,105\n2023-01-04,120\n2023-01-05,200") # 200 is outlier
    return str(p)

def test_load_data(sample_csv):
    result = load_data(sample_csv)
    data = json.loads(result)
    assert data["status"] == "success"
    assert data["rows"] == 5

def test_profile_data(sample_csv):
    result = profile_data(sample_csv)
    data = json.loads(result)
    assert "numerical_summary" in data
    assert data["rows"] == 5

def test_generate_forecast(sample_csv):
    result = generate_forecast(sample_csv, "date", "value", periods=2)
    data = json.loads(result)
    assert "forecast" in data

def test_detect_anomalies(sample_csv):
    result = detect_anomalies(sample_csv, "value", contamination=0.2)
    data = json.loads(result)
    assert "anomaly_count" in data
    # Should detect at least one anomaly (200)
    assert data["anomaly_count"] >= 1

def test_generate_report(tmp_path):
    output = tmp_path / "report.html"
    result = generate_report(
        summary="Test Summary",
        data_insights="Test Insights",
        forecast="Test Forecast",
        anomalies=["Anomaly 1"],
        strategy="Test Strategy",
        output_path=str(output)
    )
    assert "generated" in result
    assert output.exists()
