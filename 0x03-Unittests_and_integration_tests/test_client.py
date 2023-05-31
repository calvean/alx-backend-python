#!/usr/bin/env python3
""" Test the utils """

import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import client
from utils import access_nested_map, get_json, memoize
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_json_mock):
        """Test the org method of GithubOrgClient."""
        get_json_mock.return_value = expected
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)
        get_json_mock.assert_called_once_with(
          "https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """Test the _public_repos_url property of GithubOrgClient."""
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        with patch(
          'client.GithubOrgClient.org',
          new_callable=PropertyMock(return_value=payload)):
            client = GithubOrgClient("x")
            self.assertEqual(client._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """Test the public_repos method of GithubOrgClient."""
        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}
        get_json_mock.return_value = [jeff, bobb, suee]
        with patch(
          'client.GithubOrgClient._public_repos_url',
          new_callable=PropertyMock(return_value="www.yes.com")):
            client = GithubOrgClient("x")
            self.assertEqual(client.public_repos(), ['Jeff', 'Bobb', 'Suee'])
            self.assertEqual(client.public_repos("a"), ['Jeff'])
            self.assertEqual(client.public_repos("c"), [])
            self.assertEqual(client.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """Test the has_license static method of GithubOrgClient."""
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Prepare for testing."""
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda url: options.get(url, org_mock)

    @classmethod
    def tearDownClass(cls):
        """Clean up after testing."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method of GithubOrgClient."""
        client = GithubOrgClient("x")
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """Test the public_repos method of GithubOrgClient
         with a specific license."""
        client = GithubOrgClient("x")
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("NONEXISTENT"), [])
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])


if __name__ == "__main__":
    unittest.main()
