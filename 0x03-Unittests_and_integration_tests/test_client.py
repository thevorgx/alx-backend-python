#!/usr/bin/env python3
"""test_client module"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient as ghc


class TestGithubOrgClient(unittest.TestCase):
    """test class: TestGithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org: Test the org method from client.py"""
        mock_get_json.return_value = {"name": "test_org_name"}
        client = ghc(org_name)
        res = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"

        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(res, {"name": "test_org_name"})
