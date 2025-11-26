import pandas as pd
import os
import json

def load_data(file_path: str) -> str:
    """
    Loads a CSV or Excel file into a pandas DataFrame and returns a success message with basic info.
    
    Args:
        file_path (str): The absolute path to the file.
        
    Returns:
        str: JSON string with status and file info.
    """
    try:
        if not os.path.exists(file_path):
            return json.dumps({"error": f"File not found: {file_path}"})
        
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            return json.dumps({"error": "Unsupported file format. Use CSV or Excel."})
            
        return json.dumps({
            "status": "success",
            "message": f"Loaded {file_path} successfully.",
            "rows": len(df),
            "columns": list(df.columns)
        })
    except Exception as e:
        return json.dumps({"error": f"Failed to load data: {str(e)}"})
