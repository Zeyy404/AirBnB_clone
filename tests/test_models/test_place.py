#!/usr/bin/python3
"""Unit Tests for Place class"""
import unittest
import models
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing Place class"""

    def setUp(self):
        """initiate the class instance"""

        self.my_place = Place()

    def test_class_inheritance(self):
        """Test the Place class inherits from BaseModel"""

        self.assertIsInstance(self.my_place, BaseModel)

    def test_class_initiation(self):
        """Test the Place class initiate with no args"""

        self.assertEqual(Place, type(Place()))

    def test_class_attributes(self):
        """Test the User class attributes"""

        self.assertTrue(hasattr(self.my_place, "city_id"))
        self.assertTrue(hasattr(self.my_place, "user_id"))
        self.assertTrue(hasattr(self.my_place, "name"))
        self.assertTrue(hasattr(self.my_place, "description"))
        self.assertTrue(hasattr(self.my_place, "number_rooms"))
        self.assertTrue(hasattr(self.my_place, "number_bathrooms"))
        self.assertTrue(hasattr(self.my_place, "max_guest"))
        self.assertTrue(hasattr(self.my_place, "price_by_night"))
        self.assertTrue(hasattr(self.my_place, "latitude"))
        self.assertTrue(hasattr(self.my_place, "longitude"))
        self.assertTrue(hasattr(self.my_place, "amenity_ids"))

    def test_class_attributes_type(self):
        """Test the type of the User attributes"""

        self.assertTrue(isinstance(self.my_place.city_id, str))
        self.assertTrue(isinstance(self.my_place.user_id, str))
        self.assertTrue(isinstance(self.my_place.name, str))
        self.assertTrue(isinstance(self.my_place.description, str))
        self.assertTrue(isinstance(self.my_place.number_rooms, int))
        self.assertTrue(isinstance(self.my_place.number_bathrooms, int))
        self.assertTrue(isinstance(self.my_place.max_guest, int))
        self.assertTrue(isinstance(self.my_place.price_by_night, int))
        self.assertTrue(isinstance(self.my_place.latitude, float))
        self.assertTrue(isinstance(self.my_place.longitude, float))
        self.assertTrue(isinstance(self.my_place.amenity_ids, list))
        self.assertTrue(all(isinstance(x, str)
                            for x in self.my_place.amenity_ids))
