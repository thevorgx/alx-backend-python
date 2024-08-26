#!/usr/bin/env python3
"""test_utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map as anp


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
