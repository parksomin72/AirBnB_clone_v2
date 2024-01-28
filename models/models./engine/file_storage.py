#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objects_dict = json.load(f)
            for key, value in objects_dict.items():
                class_name = value["__class__"]
                obj = eval(class_name + "(**value)")
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
