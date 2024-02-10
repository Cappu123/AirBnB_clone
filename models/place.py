#!/usr/bin/python3

"""
Defining the Place class
"""
from models.base_model import BaseModel
class Place(BaseModel):
    """
    A Place class inheriting from the BaseModel class representing a place
    Attributes:
        city_id(str): and empty string to hold the value <City.id>
        user_id(str): an empty string to hold the value <User.id>
        name(str): an empty string to hold the name of the place
        description(str): desctiption of the place
        number_rooms(int): number of rooms of the place
        number_bathrooms(int): number of bathrooms in the place
        max_guest(int): number of maximum guests in the place
        price_by_night(int): price by night of the place
        latitude(float): latitude of the place
        longtude(float): longtude of the place
        amenity_ids(list): list of amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtude = 0.0
    amenity_ids = []

