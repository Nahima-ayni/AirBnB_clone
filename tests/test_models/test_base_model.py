#!/usr/bin/python3
"""
Unittest for the BaseModel class  Attributes and its methods
"""


import unittest
import uuid
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def test_new_instance(self):
        self.assertIsInstance(self.base, BaseModel)
        self.base.x = 35
        self.base.y = 50
        self.assertEqual(self.base.x, 35)
        self.assertEqual(self.base.y, 50)

    def test_id(self):
        self.assertEqual(len(self.base.id), len(str(uuid.uuid4())))
        self.assertIsInstance(uuid.UUID(self.base.id), uuid.UUID)
        self.assertIsInstance(self.base.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.created_at.day, int)
        self.assertLessEqual(self.base.created_at, datetime.datetime.now())

    def test_updated_at(self):
        self.assertIsInstance(self.base.updated_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at.day, int)
        self.assertLessEqual(self.base.updated_at, datetime.datetime.now())

    def test_has_dict(self):
        self.assertIn('__dict__', dir(self.base))

    def test_save(self):
        now = datetime.datetime.now()
        self.assertNotEqual(self.base.updated_at, now)
        self.base.save()
        now = datetime.datetime.now()
        self.assertNotEqual(now.microsecond, self.base.updated_at.microsecond)
        self.assertEqual(self.base.updated_at.second, now.second)
        self.assertEqual(self.base.updated_at.minute, now.minute)
        self.assertEqual(self.base.updated_at.hour, now.hour)
        self.assertEqual(self.base.updated_at.day, now.day)
        self.assertEqual(self.base.updated_at.month, now.month)
        self.assertEqual(self.base.updated_at.year, now.year)

    def test_to_dict(self):
        old_c_at = self.base.created_at
        old_p_at = self.base.updated_at
        r = self.base.to_dict()
        self.assertIsInstance(r, dict)
        self.assertEqual(len(r), 4)
        self.assertIn('__class__', self.base.__dict__)
        self.assertIsInstance(self.base.created_at, str)
        self.assertGreaterEqual(len(self.base.created_at), 7)
        self.assertNotEqual(self.base.created_at, old_c_at)
        self.assertNotIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, str)
        self.assertGreaterEqual(len(self.base.updated_at), 7)
        self.assertNotEqual(self.base.updated_at, old_p_at)
        self.assertNotIsInstance(self.base.updated_at, datetime.datetime)

    def test_base_return(self):
        self.assertEqual(str(self.base), "[BaseModel] ({}) \
{}".format(self.base.id, str(self.base.__dict__)))


if __name__ == "__main__":
    unittest.main()
