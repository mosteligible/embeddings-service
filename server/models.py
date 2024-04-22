from typing import List, Literal, Union

from pydantic import BaseModel


class CreateEmbedding(BaseModel):
    input: Union[str, List[str]]
    encoding_format: Literal["float", "base64"]


class Embeddings(BaseModel):
    embeddings: List[float]
    model: str
