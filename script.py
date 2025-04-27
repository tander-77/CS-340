from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password):
        """
        Initializes the MongoDB client and connects to the specified database.
        :param username: Username for MongoDB authentication
        :param password: Password for MongoDB authentication
        """
        # establish connection to MongoDB server
        self.client = MongoClient(f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:30955/?directConnection=true&appName=mongosh+1.8.0')
        # connect to AAC database
        self.database = self.client['AAC']
        
    def create(self, data):
        """
        Insert document into collection
        :param data: A dictionary representing the document to insert
        :return: True if insert is successful, False otherwise.
        """
        
        # check if data is not empty 
        if data:
            # attempt to insert the document into the collection
            result = self.database.animals.insert_one(data)
            #return True if the operation was acknowledged
            return result.acknowledged 
        else:
            # raise an error if the data parameter is empty
            raise ValueError("Data Cannot Be Empty")
            
    def read(self, query):
        """
        Query for documents in collection
        :param query: A dictionary representing the search criteria
        :return: A list of matching documents or an empty list if none is found.
        """
        
        try:
            # use the find() method to retrieve matching documents
            cursor = self.database.animals.find(query)
            # convert the cursor to a list and return the documents
            results = [document for document in cursor]
            return results
        except Exception as e:
            # print an error message if the query fails
            print(f"An error occured while reading: {e}")
            return []
        
    def update(self, query, new_values):
        """
        Update document(s) in the collection
        :param query: A dictionary representing the search criteria
        :param new_values: A dictionary representing the updated values
        :return: The number of documents modified
        """
        try:
            # use update_many to modify all matching documents
            result = self.database.animals.update_many(query, {'$set': new_values})
            # return the number of documents modified
            return result.modified_count
        except Exception as e:
            print(f"An error occured while updating: {e}")
            return 0
        
    def delete(self, query):
        """
        Delete document(s) from the collection
        :param query: A dictionary representing the search criteria
        :return: The number of documents deleted
        """
        try:
            # use delete_many to remove all matching documents
            result = self.database.animals.delete_many(query)
            # return the number of documents deleted 
            return result.deleted_count
        except Exception as e:
            print(f"An error occured while deleting: {e}")
            return 0