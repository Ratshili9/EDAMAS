import pandas as pd
import json
from tools.data_loader_tool import load_data # Re-use load logic if needed, or assume file path passed

def profile_data(file_path: str) -> str:
    """
    Generates a statistical profile of the dataset.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        str: JSON string with data profile.
    """
    try:
        df = pd.read_csv(file_path) # Simplified for now, assuming CSV
        
        profile = {
            "rows": len(df),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "dtypes": {k: str(v) for k, v in df.dtypes.items()},
            "numerical_summary": df.describe().to_dict()
        }
        
        return json.dumps(profile, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})
