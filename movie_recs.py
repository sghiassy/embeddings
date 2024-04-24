import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sentence_transformers import SentenceTransformer
import numpy

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

uri = "mongodb+srv://sghiassy:jolt39@cluster0.gantgf8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.sample_mflix
collection = db.movies

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


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
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()


for doc in collection.find({"plot_embedding_hf": {"$exists": False}, "plot": {"$exists": True}}):
    # for doc in collection.find({"plot": {"$exists": True}}):
    doc["plot_embedding_hf"] = generate_embedding_locally(doc["plot"])
    print(f"{doc['title']} = {doc['plot_embedding_hf'][:3]}")
    collection.replace_one({"_id": doc["_id"]}, doc)
