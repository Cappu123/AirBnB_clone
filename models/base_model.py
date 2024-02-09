#!/usr/bin/python3
"""
the main(base)class for the entire project
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """The base model that defines all classes in AirBnB console project

    Attributes:
        id(str): assigns a unique id when instance is created
        created_at: assigns current datetime
        updated_at: updates the current datetime

    Methods:
        __str__:  print: [<class name>] (<self.id>) <self.__dict__>
        or the class name, id and creates dictionary representation
        of the input values
        save(self): updates the instance attribute <updated_at> with the
        current datetime
        to_dict(self): returns a dictionary containing all key/value of
        <__dict__> of the instance
    """
    def __init__(self, *args, **kwargs):
        """Public instance attributes intialization after creation

        Args:
            *args(args): arguments (any), Unused
            **kwargs(dict): key/value pairs of attributes
        """
        Time_Format = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
        else:
            for key, value in kwargs.item():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, Time_Format)
                elif key[0] == "id"
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value





























