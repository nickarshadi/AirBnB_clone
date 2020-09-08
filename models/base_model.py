#!/usr/bin/python3
"""BaseModule Module."""
import uuid
import datetime
import models


class BaseModel:
    """Define all common attributes for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize Instance."""
        if kwargs and kwargs != {}:
            for k, v in kwargs.items():
                if k == 'updated_at' or k == 'created_at':
                    self.__dict__[k] = datetime.datetime.strptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print string."""
        return "[{}] ({}) {}".\
               format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys values of __dict__."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
