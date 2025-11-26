import json
import os
from typing import Any, Dict

class LongTermMemory:
    """
    Simple file-based long-term memory to persist insights across sessions.
    """
    def __init__(self, file_path: str = "memory/long_term_storage.json"):
        self.file_path = file_path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def save(self, key: str, value: Any):
        data = self.load_all()
        data[key] = value
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, key: str) -> Any:
        data = self.load_all()
        return data.get(key)

    def load_all(self) -> Dict[str, Any]:
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
