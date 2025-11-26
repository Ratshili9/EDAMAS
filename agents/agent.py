import sys
import os

# Ensure the project root is on sys.path for imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from agent import create_enterprise_analyst_agent

# Expose the root agent as expected by ADK loader
root_agent = create_enterprise_analyst_agent()
