#!/usr/bin/python3

"""
Defining the City class that inherits from the BaseModel class
"""
from models.base_model import BaseModel

class city(BaseModel):
    """
    The class to represent a city
    Attributes:
        state_id(str): empty string to hold the <State.id>
        name (str): an empty string to hold the name of the city

    """
    state_id = ""
    name = ""
