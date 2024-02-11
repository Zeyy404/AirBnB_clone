#!/usr/bin/python3
"""Unit Tests for User class"""
import unittest
import models
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Testing User class"""

    def setUp(self):
        """initiate the class instance"""

        self.my_user = User()

    def test_class_inheritance(self):
        """Test the User class inherits from BaseModel"""

        self.assertIsInstance(self.my_user, BaseModel)

    def test_class_initiation(self):
        """Test the User class initiate with no args"""

        self.assertEqual(User, type(User()))

    def test_class_attributes(self):
        """Test the User class attributes"""

        self.assertTrue(hasattr(self.my_user, "email"))
        self.assertTrue(hasattr(self.my_user, "first_name"))
        self.assertTrue(hasattr(self.my_user, "last_name"))
        self.assertTrue(hasattr(self.my_user, "password"))

    def test_class_attributes_type(self):
        """Test the type of the User attributes"""

        self.assertTrue(isinstance(self.my_user.email, str))
        self.assertTrue(isinstance(self.my_user.first_name, str))
        self.assertTrue(isinstance(self.my_user.last_name, str))
        self.assertTrue(isinstance(self.my_user.password, str))
