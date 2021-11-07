#!/usr/bin/python3
"""
Write a class called BaseModel.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    class BaseModel defines all common
    attributes/methods for other classes.
    Methods:
            save(self)
            to_dict(self)
            __str__(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization function.
        If id is not None,
        Attributes:
            id: string - assign with an uuid when an instance is created.
            created_at: datetime - assign with the current datetime
            when an instance is created.
            updated_at: datetime - assign with the current
            datetime when an instance is created and it will
            be updated every time you change your object.
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Function that prints [<class name>] (<self.id>) <self.__dict__>
        """

        return ("[{:s}] ({:s}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def to_dict(self):
        """
        Dictionary containing all keys/values of __dict__ of the instance
        """

        instance_dict = {}
        instance_dict = self.__dict__.copy()

        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
