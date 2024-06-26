#!/usr/bin/python3
"""
The module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class to represent the various cities
    
    Attributes:
        state_id (str): The State id.
        name: (str): The name of the city
    """

    state_id = ""
    name = ""
