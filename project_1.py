from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(
                self,
                username,
                password,
                host,
                port,
                db,
                collection
                ):
        # Initializing the MongoClient
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31860
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, query):
        """Query documents from the collection."""
        if query and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                return list(cursor)  # Convert cursor to a list of documents
            except errors.PyMongoError as e:
                print(f"Error querying documents: {e}")
                return []
        elif query == {}:
            return list(self.collection.find())
        else:
            raise ValueError("Invalid query: Must be a dictionary")
            
# Create method to implement the U in CRUD.
    def update(self, query, update_data):
        """Query document from collection and update."""
        if query and isinstance(query, dict) and update_data and isinstance(update_data, dict):
            try:
                result = self.collection.update_one(query, {'$set': update_data})
                print(f"Successfully updated the document.")
                return 1
            except Exception as e:
                print(f"An error occurred while updating: {e}")
        else:
            raise ValueError("Invalid query or update_data: Both must be non-empty dictionaries.")
            
# Create method to implement the D in CRUD.
    def delete(self, query):
        """Query document from collection and delete."""
        if query and isinstance(query, dict):
            try:
                cursor = self.collection.delete_one(query)
                return 1
            except errors.PyMongoError as e:
                print(f"Error deleting documents: {e}")
                return []
        else:
            raise ValueError("Invalid query: Must be a dictionary")
