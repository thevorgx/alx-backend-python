#!/usr/bin/env python3
"""test_utils module"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map as anp
from utils import get_json as gj


class TestAccessNestedMap(unittest.TestCase):
    """test class: TestAccessNestedMap
    parameterized.expand:
    test cases with expected output"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """test method to access_nested_map aka anp"""
        self.assertEqual(anp(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test method to access_nested_map aka anp
        for KeyError Raises"""
        with self.assertRaises(KeyError):
            anp(nested_map, path)


class TestGetJson(unittest.TestCase):
    """place holder for requirements"""
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    @patch('utils.get_json')
    def test_get_json(self, test_url, expected_payload, mock_get_json):
        "place holder for the other requirements"
        if test_url == 'http://example.com':
            mock_get_json.return_value = {"payload": True}
        elif test_url == 'http://holberton.io':
            mock_get_json.return_value = {"payload": False}

        res = gj(test_url)
        self.assertEqual(res, expected_payload)
        mock_get_json.assert_called_once_with(test_url)
