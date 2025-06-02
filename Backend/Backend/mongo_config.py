from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

load_dotenv(dotenv_path="../../.env")

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

if not MONGO_USERNAME or not MONGO_PASSWORD:
    raise ValueError("MONGO_USERNAME or MONGO_PASSWORD not loaded. Problem with .env file or path.")


uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster1.n76ra.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)