#!/usr/bin/python3
"""Unit Tests for State class"""
import unittest
import models
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Testing User class"""

    def setUp(self):
        """initiate the class instance"""

        self.my_state = State()

    def test_class_inheritance(self):
        """Test the State class inherits from BaseModel"""

        self.assertIsInstance(self.my_state, BaseModel)

    def test_class_initiation(self):
        """Test the State class initiate with no args"""

        self.assertEqual(State, type(State()))

    def test_class_attributes(self):
        """Test the State class attributes"""

        self.assertTrue(hasattr(self.my_state, "name"))

    def test_class_attributes_type(self):
        """Test the type of the State attributes"""

        self.assertTrue(isinstance(self.my_state.name, str))
