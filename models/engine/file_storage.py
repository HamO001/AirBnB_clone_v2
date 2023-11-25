#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
<<<<<<< HEAD
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.base_model import BaseModel
=======
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
>>>>>>> 90c523ae588975aec04d46dfbe583ac7e577444e


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Returns a dictionary of models currently in storage"""

        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)

=======
        """Returns a dictionary of models currently in storage.

        Args:
            cls (class, optional): If specified, filters the result to include
                only objects of the specified class.

        Returns:
            dict: A dictionary containing objects in storage.
        """
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
>>>>>>> 90c523ae588975aec04d46dfbe583ac7e577444e
            if cls and issubclass(cls, BaseModel):
                cls_dict = {k: v for k,
                            v in self.__objects.items() if isinstance(v, cls)}
                return cls_dict
<<<<<<< HEAD

=======
>>>>>>> 90c523ae588975aec04d46dfbe583ac7e577444e
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file."""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
<<<<<<< HEAD

    def delete(self, obj=None):
        '''Deletes obj from __objects if it's obj is
        equal to None
        '''
        if obj is None:
            return

        del_obj = f"{obj.__class__.__name__}.{obj.id}"

        try:
            del FileStorage.__objects[del_obj]
=======
        except json.decoder.JSONDecodeError:
            pass

    def delete(self, obj=None):
        """
         Delete obj from __objects if it’s inside - if obj is equal to None,
           the method should not do anything
        """
        if obj is None:
            return
        obj_to_del = f"{obj.__class__.__name__}.{obj.id}"

        try:
            del FileStorage.__objects[obj_to_del]
>>>>>>> 90c523ae588975aec04d46dfbe583ac7e577444e
        except AttributeError:
            pass
        except KeyboardInterrupt:
            pass
