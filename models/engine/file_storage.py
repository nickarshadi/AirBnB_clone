#!/usr/bin/python3
""" File Storage Module. """
import json
import datetime
import os
import models.base_model

classes = {"BaseModel": models.base_model.BaseModel}


class FileStorage():
    """Serialize instances to a JSON file and deserialize
        JSON files to a instances.

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in obj the obj with key
            <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            obj_dict = json.load(f)
            obj_dict = {k: classes[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
