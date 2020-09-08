#!/usr/bin/python3
"""Console Module."""
import cmd
import models
import json
import re
import datetime
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """Contain the entry point of the command interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Dont do anything."""
        pass

    def do_EOF(self, line):
        """Handle EOF."""
        print()
        return True

    def do_quit(self, line):
        """Exit the program."""
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel in JSON.

        Save it to JSON and print the id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in classes:
            print("** class name doesnt't exist **")
        else:
            new = classes[line]()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Print string representation of instance.

        Strig representation bases on the class name and id
        """
        args = line.split(' ')
        if line == "" or line is None:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, line):
        """Delete an instance based on class name and id."""
        args = line.split(' ')
        if line == "" or line is None:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                models.storage.all().pop(key)
                models.storage.save()

    def do_all(self, line):
        """Print all string representations of all instances."""
        if line != "":
            words = line.split(' ')
            if words[0] not in classes:
                print("** class doesn't exist **")
            else:
                objs = [str(obj) for key, obj in models.storage.all().items()
                        if type(obj).__name__ == words[0]]
                print(objs)
        else:
            objs = [str(obj) for key, obj in models.storage.all().items()]
            print(objs)

    def do_update(self, line):
        """Update an instance.

        Update based on the classs name and id by updating attributes.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name is missing **")
        elif classname not in classes:
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in models.storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = self.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(models.storage.all()[key], attribute, value)
                models.storage.all()[key].save()

    def attributes(self):
        """Return the valid attributes and their types for classname."""
        attributes = {
            "BaseModel": {
                    "id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {"name": str},
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {"name": str},
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes


if __name__ == '__main__':
    HBNBCommand().cmdloop()
