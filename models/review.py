#!/usr/bin/python3
"""A module that contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
