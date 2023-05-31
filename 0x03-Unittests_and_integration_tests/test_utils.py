#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


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

        Parameters:
          nested_map: A nested map/dictionary.
          path: A sequence of keys representing the path to the value.

        Returns:
          None, else raise AssertionError, If a KeyError is not raised
           or the exception message is not as expected.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """Test case class for the get_json function."""

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function.

        Parameters:
          test_url (str): The test URL to pass to get_json.
          test_payload (dict): The test payload to mock as the response.
          mock_get (MagicMock): The mocked get method.

        Returns:
          None, else raise AssertionError, If the mocked get method
           was not called once with the test URL or
           if the output of get_json is not equal to the test payload.
        """
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
