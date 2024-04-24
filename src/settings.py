import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DB_USERNAME = os.environ.get("db_username")
DB_PASSWORD = os.environ.get("db_password")
HF_TOKEN = os.environ.get("hf_token")
