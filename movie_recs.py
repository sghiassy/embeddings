import src.db as db
import src.model as model


def generate_embeddings():
    for doc in db.collection.find(
        {"plot_embedding_hf": {"$exists": False}, "plot": {"$exists": True}}
        # {"plot": {"$exists": True}}
    ):
        doc["plot_embedding_hf"] = model.generate_embedding_locally(doc["plot"])
        print(f"{doc['title']} = {doc['plot_embedding_hf'][:3]}")
        db.collection.replace_one({"_id": doc["_id"]}, doc)


def search_embeddings():
    query = "imaginary characters from outer space at war"
    results = db.collection.aggregate([{
        "$vectorSearch": {
            "queryVector": model.generate_embedding_locally(query),
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": 4,
            "index": "PlotSemanticSearch",
        }
    }])

    for document in results:
        print(f"Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n")


search_embeddings()
