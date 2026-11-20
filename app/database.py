
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGODB_URL)

database = client[DATABASE_NAME]

employee_collection = database["employees"]


def check_database_connection():
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
