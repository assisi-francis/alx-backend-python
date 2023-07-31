#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")

For each of these inputs, test with assertEqual that the function returns the expected result.

The body of the test method should not be longer than 2 lines.
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        expected_error_message = f"Key not found: '{path[-1]}'"
        self.assertEqual(str(context.exception), expected_error_message)

if __name__ == "__main__":
    unittest.main()
