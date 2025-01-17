#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from os import getenv


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertNotEqual(type(new.state_id), str)
        else:
            self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertNotEqual(type(new.name), str)
        else:
            self.assertEqual(type(new.name), str)
