#!/usr/bin/python3
"""test for the console"""

import unittest
from console import HBNBCommand
import sys
import io


class Test(unittest.TestCase):
    def test_create_instance(self):
        """tests the output when giving a specific id at creation"""

        output = io.StringIO()
        sys.stdout = output
        console = HBNBCommand()
        console.onecmd("create City id='hello_Antoine'\
                       name=laval\
                       state_id=00d8b06b-ce0c-48f9-b4b5-5abc905d9408")
        sys.stdout = sys.__stdout__
        expected_output = output.getvalue()
        self.assertIn("hello Antoine", expected_output)
