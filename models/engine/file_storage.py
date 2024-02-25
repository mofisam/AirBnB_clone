#!/usr/bin/python3

"""
Defines the FileStorage class for serializing and deserializing instances.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Serializes instances to JSON and deserializes back to instance objects."""

    __objects = {}  # Stores all objects by <class name>.id
    __file_path = "file.json"  # Path to the JSON file.

    def all(self, cls=None):
        """Returns a dictionary of all objects."""
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Adds a new object to __objects."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the file exists).

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            Exception: If an error occurs during deserialization.
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                class_name = obj_data["__class__"]
                del obj_data["__class__"]
                self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
