#!/usr/bin/env python3
""" TEST Cases Module """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case class for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient."""
        expected_result = {
          "name": org_name, "description": "Test org"}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        result = client.org()

        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(
          f"https://api.github.com/orgs/{org_name}")


if __name__ == "__main__":
    unittest.main()
