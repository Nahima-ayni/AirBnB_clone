#!/usr/bin/python3

"""import modules"""
import json
import os


class FileStorage:
    """
        Initialize the private class instance.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self, filename="file.json"):
        self.filename = filename

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
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({
                k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
            Load data from the JSON file and populate the storage dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    del value['__class__']
                    module = __import__(
                            'models.' + cls_name.lower(), fromlist=[cls_name])
                    cls = getattr(module, cls_name)
                    self.new(cls(**value))
        except FileNotFoundError:
            pass
