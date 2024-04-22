from pathlib import Path

import config
from sentence_transformers import SentenceTransformer


def set_transformer_model(model_name: str):
    global model
    config.LLM_MODEL_PATH = Path("/srv") / model_name
    model = SentenceTransformer(model_name_or_path=str(config.LLM_MODEL_PATH))


model = SentenceTransformer(model_name_or_path=str(config.LLM_MODEL_PATH))
