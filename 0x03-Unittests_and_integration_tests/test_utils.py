#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function.

        Parameters:
          test_url (str): The test URL to pass to get_json.
          test_payload (dict): The test payload to mock as the response.
          mock_get (MagicMock): The mocked requests.get method.

        Returns:
          None

        Raises:
          AssertionError: If the output of get_json
           is not equal to the test payload.
        """
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)


class TestMemoize(unittest.TestCase):
    """Test case class for the memoize decorator."""

    def test_memoize(self):
        """
        Test the memoize decorator.

        Returns:
          None

        Raises:
          AssertionError: If the correct result
           is not returned when calling a_property twice
                          or if a_method is called more than once.
        """
        class TestClass:
            """ test class used """
            def a_method(self):
                """ a method to return 42 """
                return 42

            @memoize
            def a_property(self):
                """ a property to return a method """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()

            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()
