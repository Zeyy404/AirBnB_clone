#!/usr/bin/python3
"""Unit Tests for Review class"""
import unittest
import models
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing Review class"""

    def setUp(self):
        """initiate the class instance"""

        self.my_review = Review()

    def test_class_inheritance(self):
        """Test the Review class inherits from BaseModel"""

        self.assertIsInstance(self.my_review, BaseModel)

    def test_class_initiation(self):
        """Test the Review class initiate with no args"""

        self.assertEqual(Review, type(Review()))

    def test_class_attributes(self):
        """Test the Review class attributes"""

        self.assertTrue(hasattr(self.my_review, "place_id"))
        self.assertTrue(hasattr(self.my_review, "user_id"))
        self.assertTrue(hasattr(self.my_review, "text"))

    def test_class_attributes_type(self):
        """Test the type of the Review attributes"""

        self.assertTrue(isinstance(self.my_review.place_id, str))
        self.assertTrue(isinstance(self.my_review.user_id, str))
        self.assertTrue(isinstance(self.my_review.text, str))
