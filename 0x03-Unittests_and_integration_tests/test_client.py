#!/usr/bin/env python3
""" TEST Cases Module """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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
            org_name (str): The name of the organization.
            mock_get_json (Mock): The patched get_json function.

        Returns:
            None. Raises AssertionError if the test fails.
        """
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(
          f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, mock_get_json.return_value)

    def test_public_repos_url(self):
        """
        Test the _public_repos_url property of GithubOrgClient.

        Returns:
            None. Raises AssertionError if the test fails.
        """
        client = GithubOrgClient("test_org")
        with patch.object(
          GithubOrgClient,
          "org",
          new_callable=PropertyMock(return_value={"repos_url": "test_url"})):
            result = client._public_repos_url
            self.assertEqual(result, "test_url")

    @patch(
      'client.get_json',
      return_value=[{"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json):
        """
        Test the public_repos method of GithubOrgClient.

        Args:
            mock_get_json (Mock): The patched get_json function.

        Returns:
            None. Raises AssertionError if the test fails.
        """
        client = GithubOrgClient("test_org")

        result = client.public_repos()
        mock_get_json.assert_called_once_with(client._public_repos_url)
        self.assertEqual(result, ["repo1", "repo2"])


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test case class for integration tests of GithubOrgClient."""

    @parameterized.expand(TEST_PAYLOAD)
    @patch('requests.get', side_effect=HTTPError)
    def test_public_repos(
      self,
      org_payload,
      repos_payload,
      expected_repos,
      apache2_repos,
      mock_requests_get):
        """
        Test the public_repos method of GithubOrgClient
         with real HTTP requests.

        Args:
            org_payload (dict): The organization payload.
            repos_payload (list): The repository payload.
            expected_repos (list): The expected list of repositories.
            apache2_repos (list): The expected list
             of repositories with Apache2 license.
            mock_requests_get (Mock): The patched requests.get function.

        Returns:
            None. Raises AssertionError if the test fails.
        """
        client = GithubOrgClient("test_org")
        mock_requests_get.return_value.json.side_effect = [
          org_payload, repos_payload]
        result = client.public_repos()
        self.assertEqual(result, expected_repos)
