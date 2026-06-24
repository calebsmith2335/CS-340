from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter:
    """CRUD operations for the AAC animal collection in MongoDB."""

    def __init__(self, username, password):
        # Connect to MongoDB using the aacuser credentials
        self.client = MongoClient(
            f"mongodb://{username}:{password}@localhost:27017/aac?authSource=admin"
        )

        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert a document into the animals collection."""
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return result.inserted_id is not None
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, query):
        """Query documents from the animals collection."""
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print("Error reading documents:", e)
                return []
        else:
            raise Exception("Query parameter is empty")
        
    def update(self, query, new_values):
        """Update document(s) in the animals collection."""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, new_values)
                return result.modified_count
            except Exception as e:
                print("Error updating documents:", e)
                return 0
        else:
            raise Exception("Query or update values are empty")
            
    def delete(self, query):
        """Delete document(s) from the animals collection."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Error deleting documents:", e)
                return 0
        else:
            raise Exception("Query parameter is empty")