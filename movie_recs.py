import src.db as db
import src.model as model

for doc in db.collection.find(
    {"plot_embedding_hf": {"$exists": False}, "plot": {"$exists": True}}
):
    doc["plot_embedding_hf"] = model.generate_embedding_locally(doc["plot"])
    print(f"{doc['title']} = {doc['plot_embedding_hf'][:3]}")
    db.collection.replace_one({"_id": doc["_id"]}, doc)
