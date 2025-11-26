import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import json

def generate_forecast(file_path: str, date_col: str, value_col: str, periods: int = 3) -> str:
    """
    Generates a forecast using Exponential Smoothing.
    
    Args:
        file_path (str): Path to CSV.
        date_col (str): Name of the date column.
        value_col (str): Name of the value column to forecast.
        periods (int): Number of periods to forecast.
        
    Returns:
        str: JSON string with forecast data.
    """
    try:
        df = pd.read_csv(file_path)
        if date_col not in df.columns or value_col not in df.columns:
            return json.dumps({"error": f"Columns {date_col} or {value_col} not found."})
            
        df[date_col] = pd.to_datetime(df[date_col])
        df = df.sort_values(by=date_col)
        df = df.set_index(date_col)
        
        # Simple Holt-Winters
        model = ExponentialSmoothing(df[value_col], trend='add', seasonal=None).fit()
        forecast = model.forecast(periods)
        
        # Convert series to dict with string keys for JSON serialization
        forecast_dict = {str(k): v for k, v in forecast.to_dict().items()}
        
        return json.dumps({
            "forecast": forecast_dict,
            "model_info": "Exponential Smoothing (Holt-Winters)"
        })
    except Exception as e:
        return json.dumps({"error": str(e)})
