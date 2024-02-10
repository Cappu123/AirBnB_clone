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
    
    def new(self, object):
        """
        Sets in __objects the obj with key <obj class name>.id
         (ex: to store a BaseModel object with id=12121212, the key will be a       seModel.12121212)
         Args:
            object(obj): object to write
        """
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object
    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        with open(self.file_path, 'w+') as f:
            json.dump({key: value.to_dect() for key, value in self__objects.items()}, f)
             def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
