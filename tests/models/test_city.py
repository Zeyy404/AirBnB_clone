#!/usr/bin/python3
"""Unit Tests for City class"""
import unittest
import models
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Testing City class"""

    def setUp(self):
        """initiate the class instance"""

        self.my_city = City()

    def test_class_inheritance(self):
        """Test the City class inherits from BaseModel"""

        self.assertIsInstance(self.my_city, BaseModel)

    def test_class_initiation(self):
        """Test the City class initiate with no args"""

        self.assertEqual(City, type(City()))

    def test_class_attributes(self):
        """Test the City class attributes"""

        self.assertTrue(hasattr(self.my_city, "state_id"))
        self.assertTrue(hasattr(self.my_city, "name"))

    def test_class_attributes_type(self):
        """Test the type of the City attributes"""

        self.assertTrue(isinstance(self.my_city.state_id, str))
        self.assertTrue(isinstance(self.my_city.name, str))
