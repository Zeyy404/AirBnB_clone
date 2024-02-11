#!/usr/bin/python3
"""Unit test for BaseModel class"""
import unittest
import models
import datetime
from io import StringIO
import sys
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel class"""

    def setUp(self):
        """Initializing class instance"""
        self.my_model = BaseModel()

    def tearDown(self):
        """Delete class instance"""
        del self.my_model

    def test_id_type(self):
        """Test the type of the id assigned is string"""
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_uniqueness(self):
        """Test the ids assigned are different from an instance to another"""

        my_model_ = BaseModel()
        self.assertNotEqual(my_model_.id, self.my_model.id)

    def test_created_at_type(self):
        """Test the type of the value of created_at"""

        self.assertTrue(isinstance(self.my_model.created_at,
                                   datetime.datetime))

    def test_updated_at_type(self):
        """Test the type of the value of updated_at"""

        self.assertTrue(isinstance(self.my_model.updated_at,
                                   datetime.datetime))

    def test_save_method(self):
        """Testing the save() method if it changes the date
                         of the updated_at attribute.
        """

        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_updated_at)

    def test_str_overide(self):
        """Testing that the right message gets printed."""

        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        """Testing the type of instance of the to_dict method"""

        self.assertTrue("<class 'dict'>", type(self.my_model.to_dict))
