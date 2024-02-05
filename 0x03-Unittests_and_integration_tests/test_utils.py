#!/usr/bin/env python3
"""
Test cases for the utils module
"""
import utils
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    a class that inherits from unittest.TestCase
    and implements tests for the utils module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        tests access_nested_map() returns valid output
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        tests if access_nested_map() raises a KeyError exception
        """
        with self.assertRaises(expected):
            utils.access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
