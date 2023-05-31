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
        """
        Test the org method of GithubOrgClient.

        Args:
            org_name: The name of the organization.
            mock_get_json: The patched get_json function.

        Returns:
            None. Raises AssertionError if the test fails.
        """
        client = GithubOrgClient(org_name)

        result = client.org()

        mock_get_json.assert_called_once_with(
          f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, mock_get_json.return_value)


if __name__ == "__main__":
    unittest.main()
