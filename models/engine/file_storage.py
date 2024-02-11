#!/usr/bin/python3

"""import modules"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        Initialize the private class instance.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Return the dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
            Add a new object to the storage dictionary.
        """
        class_name = obj.__class__.__name__
        object_id = obj.id
        key = f"{class_name}.{object_id}"
        self.__objects[key] = obj

    def save(self):
        """
            Serialize the storage dictionary and save it to the JSON file.
        """
        dic = {}
        for key, obj in self.all().items():
            dic[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dic, text_file)

    def reload(self):
        """
            Load data from the JSON file and populate the storage dictionary.
        """
        classes = {
                'BaseModel': BaseModel,
                    'User': User,
                    'Amenity': Amenity,
                    'City': City,
                    'Place': Place,
                    'State': State,
                    'Review': Review,
            }
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                dic = json.load(f)

                for key, val in dic.items():
                    class_name = val['__class__']
                    class_inst = classes[class_name]
                    instance = class_inst(**val)
                    all_obj = self.all()
                    all_obj[key] = instance
        except FileNotFoundError:
            pass
