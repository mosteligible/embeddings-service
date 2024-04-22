import base64
import json
from typing import List


def encode_base64(embeddings: List[float]) -> str:
    encoded_embeddings = json.dump(embeddings).encode()
    base64_str = base64.encodebytes(encoded_embeddings)
    return base64_str
