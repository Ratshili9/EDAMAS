import pandas as pd
import os

def validate_csv(file_path: str) -> bool:
    """Validates if a file is a valid CSV and not empty."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("CSV file is empty.")
        return True
    except Exception as e:
        raise ValueError(f"Invalid CSV file: {str(e)}")

def validate_dataframe(df: pd.DataFrame, required_columns: list[str] = None) -> bool:
    """Validates a DataFrame structure."""
    if df.empty:
        raise ValueError("DataFrame is empty.")
    
    if required_columns:
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
    
    return True
