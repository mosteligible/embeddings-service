import config
import transformer
import utils
from fastapi import FastAPI
from models import CreateEmbedding, Embeddings

app = FastAPI(title="Embedding Service", version="0.1.0")


@app.post("/embedding", response_model=Embeddings)
async def get_embedding(data: CreateEmbedding):
    input_text = data.input
    embeddings = transformer.model.encode(input_text)
    if data.encoding_format == "base64":
        embeddings = utils.encode_base64(embeddings)
    resp = Embeddings(embeddings=embeddings, model=config.LLM_MODEL_NAME)
    return resp


@app.post("/set-default-model")
async def set_model(name: str):

    return {"Success": True, "model": name}
