#!/usr/bin/python3
"""
a file storage that serializes instances to JSON file to store and
deserializes stored file back to instances
"""
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    The file storage class

    Class attributes(Private):
        __file_path(str): path to the JSON file(Ex: file.json)
        __objects{}: an empty dictionary to store- all objects by
        <class name>.id
    """
    __file_path = "file.json"
    __objects = {}
    
    
    def all(self):
        """
        Returns a dictionary of all objects
        """
        return self.__objects
    
    def
