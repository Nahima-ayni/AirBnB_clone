#!/usr/bin/python3

"""import modules"""
import json
import datetime


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
        return FileStorage.__objects

    def new(self, obj):
        """
            Add a new object to the storage dictionary.
        """
        class_name = obj.__class__.__name__
        object_id = obj.id
        key = f"{class_name}.{object_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Serialize the storage dictionary and save it to the JSON file.
        """
        dic = {}
        for key, obj in self.all().items():
            dic[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dic, f)

    def classes(self):
        """
            All the Classes are stored in a dictionary and then returens the dictionary.
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
        return classes

    def reload(self):
        """
            Load data from the JSON file and populate the storage dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                dic = json.load(f)

                for key, val in dic.items():
                    class_name = val['__class__']
                    class_inst = classes[class_name]
                    instance = class_inst(**val)
                    all_obj = self.all()
                    all_obj[key] = instance
        except FileNotFoundError:
            pass

    def attributes(self):
		"""Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
