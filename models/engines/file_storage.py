import json
import os


class FileStorage:
    def __init__(self, file_path):
        """
            Initialize the private class instance.
        """
        self.__file_path = file_path
        self.__objects = {}

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
        json_string = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as file:
            file.write(json_string)

    def reload(self):
        """
            Load data from the JSON file and populate the storage dictionary.
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    data = json.load(file)
                    self.__objects = data
            except FileNotFoundError:
                pass
