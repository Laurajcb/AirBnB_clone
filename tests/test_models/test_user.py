#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
import json
import os
from models import TestUser
from models import user
User = user.User


class TestUser(unittest.TestCase):
    """This class contains several methods to test the
    user.py file.
    """
