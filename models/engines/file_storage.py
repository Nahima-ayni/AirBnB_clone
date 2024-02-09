import json
import os


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
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
            Load data from the JSON file and populate the storage dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, value in serialized_objects.items():
                    clas_name, obj_id = key.split('.')
                    obj= eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
