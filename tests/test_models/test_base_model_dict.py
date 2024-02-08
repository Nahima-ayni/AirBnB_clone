#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_to_dict(unittest.TestCase):

    def test_init_with_kwargs(self):
        """Test initializing with kwargs"""
        data = {
            'id': '1',
            'created_at': '2024-02-08T12:00:00.000000',
            'updated_at': '2024-02-08T12:00:00.000000',
            'name': 'test_object'
        }
        obj = BaseModel(**data)

        self.assertEqual(obj.id, '1')
        self.assertEqual(obj.created_at, datetime(2024, 2, 8, 12, 0))
        self.assertEqual(obj.updated_at, datetime(2024, 2, 8, 12, 0))
        self.assertEqual(obj.name, 'test_object')

    def test_init_without_kwargs(self):
        """Test initializing without kwargs"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(isinstance(obj.created_at, datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime))

    def test_to_dict_method(self):
        """Test to_dict() method"""
        obj = BaseModel(id='1', created_at=datetime(2024, 2, 8, 12, 0), updated_at=datetime(2024, 2, 8, 12, 0))
        expected_dict = {
            '_class_': 'BaseModel',
            'id': '1',
            'created_at': '2024-02-08T12:00:00',
            'updated_at': '2024-02-08T12:00:00'
        }
        self.assertDictEqual(obj.to_dict(), expected_dict)

    def test_str_method(self):
        """Test __str__() method"""
        obj = BaseModel(id='1', created_at=datetime(2024, 2, 7, 12, 0), updated_at=datetime(2024, 2, 7, 12, 0))
        expected_str = "[BaseModel] (1) {'id': '1', 'created_at': datetime.datetime(2024, 2, 7, 12, 0), 'updated_at': datetime.datetime(2024, 2, 7, 12, 0)}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """Test save() method"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_equality(self):
        """Test equality between BaseModel instances"""
        obj1 = BaseModel(id='1')
        obj2 = BaseModel(id='1')
        self.assertEqual(obj1, obj2)

    def test_non_equality(self):
        """Test non-equality between BaseModel instances with different IDs"""
        obj1 = BaseModel(id='1')
        obj2 = BaseModel(id='2')
        self.assertNotEqual(obj1, obj2)

    def test_non_equality_with_other_class(self):
        """Test non-equality between BaseModel instance and instance of another class"""
        obj1 = BaseModel(id='1')
        obj2 = SomeOtherClass(id='1')
        self.assertNotEqual(obj1, obj2)


if __name__ == '__main__':
    unittest.main()
