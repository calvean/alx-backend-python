#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case class for the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function.

        Args:
          nested_map: A nested map/dictionary.
          path: A sequence of keys representing the path to the value.
          expected_result: The expected result of accessing the nested map.

        Returns:
          None, else raises AssertionError, If the returned value
           is not equal to the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that a KeyError is raised when accessing a non-existing key.

        Args:
          nested_map: A nested map/dictionary.
          path: A sequence of keys representing the path to the value.

        Returns:
          None, else raise AssertionError: If a KeyError is not raised
           or the exception message is not as expected.
        """

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        actual_exception_msg = str(context.exception)

        expected_exception_msg = f"KeyError: Key not found: {path[-1]}"

        self.assertEqual(actual_exception_msg, expected_exception_msg)
