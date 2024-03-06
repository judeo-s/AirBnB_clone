#!/usr/bin/python3

'''A module used to act as a base for other modules'''

from datetime import datetime
import json
from uuid import uuid4


class BaseModel:
    '''
    A base class that defines all common attributes/methods for other classes
    '''

    def __init__(self):
        '''A constructor function for the BaseModel class'''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''
        An method that returns a custom string representing the class

        Returns:
            str
        '''
        return f'[{BaseModel.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''
        A method that updates the updated_at with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        A function that returns a dictionary containing all key/values of
        __dict__ of the instance

        Return:
            dict
        '''
        class_dict = {}
        class_dict.update(self.__dict__)
        class_dict['created_at'] = class_dict['created_at'].isoformat()
        class_dict['updated_at'] = class_dict['updated_at'].isoformat()
        return class_dict
