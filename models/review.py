#!/usr/bin/python3
"""
Defining the Review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    A sub class of basemodel representing a review

    Attributes:
    place_id(str): an empty string to hold the value <Place.id>
    user_id(str): an empty string to hold the value <User.id>
    text(str): and empty string
    """

    place_id = ""
    user_id = ""
    text = ""
