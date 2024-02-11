#!/usr/bin/python3
"""Unit Tests for Amenity class"""
import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity class"""

    def setUp(self):
        """initiate the class instance"""

        self.my_amenity = Amenity()

    def test_class_inheritance(self):
        """Test the Amenity class inherits from BaseModel"""

        self.assertIsInstance(self.my_amenity, BaseModel)

    def test_class_initiation(self):
        """Test the Amenity class initiate with no args"""

        self.assertEqual(Amenity, type(Amenity()))

    def test_class_attributes(self):
        """Test the Amenity class attributes"""

        self.assertTrue(hasattr(self.my_amenity, "name"))

    def test_class_attributes_type(self):
        """Test the type of the Amenity attributes"""

        self.assertTrue(isinstance(self.my_amenity.name, str))
