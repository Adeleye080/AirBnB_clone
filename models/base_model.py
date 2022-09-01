#!/usr/bin/python3
""" Basemodel module """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common methods for other classes
    """
    def __init__(self, *args):
        """ initialisation of the class BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
        __dict__ of the instance """
        dict1 = self.__dict__.copy()
        dict1['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict1['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict1['__class__'] = self.__class__.__name__
        return dict1

    def __str__(self):
        """ prints  a string repr """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"