#!/usr/bin/python3

"""
    imports necessary modules
"""
import unittest
import uuid
import sys
import os

# Ensure that the parent directory is in the PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
grand_parent_dir = os.path.abspath(os.path.join(parent_dir, '..'))
sys.path.insert(0, parent_dir)
sys.path.insert(0, grand_parent_dir)

# Import BaseModel from the models module
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""
    def test_instance_attributes(self):
        """Test if the BaseModel instance has the required attributes."""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))



    def test_instance_methods(self):
        """Test if the BaseModel instance has the required methods."""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'save'))
        self.assertTrue(hasattr(base_model, 'to_dict'))
        self.assertTrue(callable(getattr(base_model, 'save')))
        self.assertTrue(callable(getattr(base_model, 'to_dict')))

    def test_save_method(self):
        """Test if the save() method updates the updated_at attribute."""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()

    def test_to_dict_method(self):
        """Test if the to_dict() method returns the expected dictionary format."""
        base_model = BaseModel()
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(base_model_dict['created_at']), str)
        self.assertEqual(type(base_model_dict['updated_at']), str)

    def test_init_method(self):
        """Test if the __init__() method initializes attributes correctly."""
        now = datetime.now()
        base_model = BaseModel(created_at=now.isoformat(), updated_at=now.isoformat())
        self.assertEqual(type(base_model.created_at), datetime)
        self.assertEqual(type(base_model.created_at), datetime)


    def test_str_method(self):
        """Test if the __str__() method generates the expected string representation."""
        base_model = BaseModel()
        self.assertEqual(str(base_model), "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__))


    def test_id(self):
        """Test if the id attribute is unique for each BaseModel instance."""
        base_model_01 = BaseModel()
        base_model_02 = BaseModel()

        self.assertNotEqual(base_model_01.id, base_model_02.id)

if __name__ == '__main__':
    unittest.main()
