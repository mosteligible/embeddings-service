import os
from pathlib import Path

SERVER_DIR = Path(__file__).parent.absolute()
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")
LLM_MODEL_PATH = Path("/srv") / LLM_MODEL_NAME
