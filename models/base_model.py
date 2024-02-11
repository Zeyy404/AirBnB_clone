#!/usr/bin/python3
"""A module that defines the BaseModel

   BaseModel (class): defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The base model class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints the string representation of an object's information"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute
             updated_at with the current datetime

           Calls save(self) method of the storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary represenation of an instance"""
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__

        if 'created_at' in result_dict:
            result_dict['created_at'] = result_dict['created_at'].isoformat()
        if 'updated_at' in result_dict:
            result_dict['updated_at'] = result_dict['updated_at'].isoformat()

        return result_dict
