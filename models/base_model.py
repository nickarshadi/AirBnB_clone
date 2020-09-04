#!/usr/bin/python3
import math
import uuid
import datetime
""" BaseModule Module. """


class BaseModel:
    """ Define all common attributes for other classes. """

    def __init__(self):
        """ Constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ str """
        return "[{}] ({}) {}".\
               format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Update updated_at. """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Return a dictionary containing all keys values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = datetime.datetime.now().isoformat()
        return my_dict
