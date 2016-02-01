from pymongo import MongoClient


client = MongoClient()
db = client.flask_db
collection = db.flask_collection

