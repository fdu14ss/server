from pymongo import MongoClient


client = MongoClient(connect=False)
db = client.flask_db

