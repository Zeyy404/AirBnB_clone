#!/usr/bin/python3
"""Defines the FileStorage class that serializes instances to a JSON file
   and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """The file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {}
        for obj_id, obj_data in self.__objects.items():
            data[obj_id] = obj_data.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(data, f)

    def class_(self):
        """Returns a dictionary representation of classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_ = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        return class_

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for obj_id, obj_data in data.items():
                    obj = self.class_()[obj_data["__class__"]](**obj_data)
                    self.__objects[obj_id] = obj
