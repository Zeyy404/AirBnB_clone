#!/usr/bin/python3
"""A module that contains City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherits from BaseModel"""

    state_id = ""
    name = ""
