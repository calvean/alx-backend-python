#!/usr/bin/env python3
""" TEST Cases Module """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    """Test case class for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value=TEST_PAYLOAD)
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient."""
        client = GithubOrgClient(org_name)
        result = client.org()
        self.assertEqual(result, TEST_PAYLOAD)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test the _public_repos_url property of GithubOrgClient."""
        org_name = "holberton"
        repos_url = f"https://api.github.com/orgs/{org_name}/repos"

        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock, return_value={"repos_url": repos_url}) as mock_org:
            client = GithubOrgClient(org_name)
            result = client._public_repos_url
            self.assertEqual(result, repos_url)
            mock_org.assert_called_once

    @patch('client.get_json', return_value=TEST_PAYLOAD)
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient."""
        org_name = "holberton"
        license_key = "MIT"
        expected_repos = ["repo1", "repo2"]

        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock, return_value="https://api.github.com/repos") as mock_repos_url:
            client = GithubOrgClient(org_name)
            result = client.public_repos(license=license_key)
            self.assertEqual(result, expected_repos)
            mock_get_json.assert_called_once_with("https://api.github.com/repos")
            mock_repos_url.assert_called_once

if __name__ == "__main__":
    unittest.main()

