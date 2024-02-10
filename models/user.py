#!/usr/bin/python3
from models.base_model import BaseModel
"""
Defining the User class that inherits from the BaseModel
"""
class User(BaseModel):
    """
    A user:

    Attributes:
        email(str): empty string to for the user email
        password(str): an empty string for the user password
        first_name(str): an empty string for the user's first name
        last_name(str): an empty string for the user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

