#!/usr/bin/python3

'''A model that is used to test the BaseModel class'''


import inspect
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestDocumentation(unittest.TestCase):
    '''Tests the documentation for modules, classes, and methods.'''

    @classmethod
    def setUpClass(cls):
        '''
        Set up class method for doc tests.
        '''
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring_exists(self):
        '''
        Tests if module docstring documentation exists.
        '''
        self.assertIsNotNone(BaseModel.__doc__)

    def test_classes_docstring_exists(self):
        '''
        Tests if class docstring documentation exists.
        '''
        self.assertIsNotNone(BaseModel.__doc__.__class__)

    def test_methods_docstring_exists(self):
        '''
        Tests if methods docstring documentation exists
        '''
        for _, method in self.setup:
            self.assertIsNotNone(method.__doc__)


class TestBaseModel(unittest.TestCase):
    '''A class dedicated to testing the BaseModel class'''

    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        '''
        A function that tests the __init__ function of the BaseModel class
        '''
        # Test ID generation
        self.assertIsInstance(self.base_model.id, str)
        self.assertTrue(len(self.base_model.id) == 36)

        # Test datetime attributes
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(
                self.base_model.created_at, self.base_model.updated_at)

    def test_str(self):
        '''
        A function that tests the __str__ function in the BaseModel class
        '''
        name = BaseModel.__name__
        ID = self.base_model.id
        cls_dict = self.base_model.__dict__
        expected_string = f'[{name}] ({ID}) {cls_dict}'
        self.assertEqual(str(self.base_model), expected_string)

    def test_save(self):
        '''
        A function that tests the save method in the BaseModel class
        '''
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        '''
        A function to test the to_dict method in the BaseModel class
        '''
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)
