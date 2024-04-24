import requests
from sentence_transformers import SentenceTransformer
import numpy

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def generate_embedding_locally(text: str) -> list[float]:
    np: numpy = model.encode(text)
    return np.tolist()


def generate_embedding_remotely(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text},
    )

    if response.status_code != 200:
        raise ValueError(
            f"Request failed with status code {response.status_code}: {response.text}"
        )

    return response.json()
