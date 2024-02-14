#!/usr/bin/python3
"""unit tests for the file_storage module"""
import unittest
import os
from io import StringIO
import json
import sys
sys.path.append('../../')
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

    def test_save(self, mock_json_dump, mock_open):
        """File_storage"""
        self.storage.new(self.base_model)
        self.storage.save()
        mock_open.assert_called_once_with((FileStorage._FileStorage__file_path,
                                           "w", encoding="utf-8"))
        mock_json_dump.assert_called_once()

    def test_all(self):
        """File_storage"""
        self.storage.new(self.base_model)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)

    def test_new_method(self):
        """Tests that the new method sets the right key and value pair
            in the FileStorage.__object attribute.
        """

        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_reload_empty(self, mock_open, mock_stat):
        """File_storage"""
        mock_stat.return_value.st_size = 0
        self.storage.reload()
        self.assertFalse(self.storage._FileStorage__objects)

    def test_reload_with_data(self, mock_open):
        """File_storage"""
        self.storage.reload()
        self.assertTrue(self.storage._FileStorage__objects)
        key = "BaseModel.1234"
        self.assertIn(key, self.storage._FileStorage__objects)
        obj = self.storage._FileStorage__objects[key]
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, "1234")

     def test_reload_not_found(self, mock_open):
         """File_storage"""
         self.storage.reload()
         mock_open.assert_called_once_with((FileStorage._FileStorage__file_path,
                                            "r+", encoding="utf-8"))
         self.assertFalse(self.storage._FileStorage__objects)

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
