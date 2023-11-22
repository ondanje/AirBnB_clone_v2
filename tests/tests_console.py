import unittest
from datetime import datetime
import json
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os


class TestConsole(unittest.TestCase):
    """TestConsole class
    Args:
        unittest (): Test property
    """

    def test_module_doc(self):
        """Module documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """Class doc"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)