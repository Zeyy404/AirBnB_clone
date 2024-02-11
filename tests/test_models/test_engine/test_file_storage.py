#!/usr/bin/python3
"""unit tests for the file_storage module"""
import os
import json
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage class"""

    def setUp(self):
        """Initializing classes"""

        self.my_model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """Cleans up after testing is done"""

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_FileStorage_instializing(self):
        """Test initializing with no args"""

        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation(self):
        """Test initializing with args"""

        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_attributes(self):
        """Test the class attributes types"""

        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all_return_type(self):
        """Tests the data type of the return value of the all method."""

        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        """Tests that the new method sets the right key and value pair
            in the FileStorage.__object attribute.
        """

        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        """Tests that the type of value contained in the FileStorage.__object
            is of type obj.__class__.__name__
        """

        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        """Tests that a file gets created with the name file.json"""

        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))
