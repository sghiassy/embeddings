import src.settings as settings
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = f"mongodb+srv://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@cluster0.gantgf8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.sample_mflix
movies = db.movies
embedded_movies = db.embedded_movies
