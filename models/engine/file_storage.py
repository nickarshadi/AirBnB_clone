#!/usr/bin/python3
""" File Storage Module. """
import json
import datetime
import os


class FileStorage():
    """ Serialize instances to a JSON file and deserialize
        JSON files to a instances. """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in obj the obj with key
            <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to JSON file. """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects.items(), f)

    def reload(self):
        """ Deserialize the JSON file to __objects. """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            FileStorage.__objects = json.loads(f)
