import pandas as pd
from sklearn.ensemble import IsolationForest
import json

def detect_anomalies(file_path: str, value_col: str, contamination: float = 0.05) -> str:
    """
    Detects anomalies using Isolation Forest.
    
    Args:
        file_path (str): Path to CSV.
        value_col (str): Column to check for anomalies.
        contamination (float): Expected proportion of outliers.
        
    Returns:
        str: JSON string with anomalies.
    """
    try:
        df = pd.read_csv(file_path)
        if value_col not in df.columns:
            return json.dumps({"error": f"Column {value_col} not found."})
            
        data = df[[value_col]].dropna()
        clf = IsolationForest(contamination=contamination, random_state=42)
        df['anomaly_score'] = clf.fit_predict(data)
        
        anomalies = df[df['anomaly_score'] == -1]
        
        return json.dumps({
            "anomaly_count": len(anomalies),
            "anomalies": anomalies.to_dict(orient='records')
        })
    except Exception as e:
        return json.dumps({"error": str(e)})
