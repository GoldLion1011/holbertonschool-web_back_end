#!/usr/bin/env python3
""" Unittests and integration tests for client.py """


import unittest
from unittest.mock import patch, PropertyMock
from urllib.error import HTTPError
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient Class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        """ Test org method """
        mock_get_json.return_value = {"payload": True}
        test_class = GithubOrgClient(test_org_name)
        self.assertEqual(test_class.org, mock_get_json.return_value)
        mock_get_json.assert_called_once()

    # @classmethod
    # def setUpClass(cls):
    #     """ setUpClass method """
    #     cls.get_patcher = patch('requests.get', side_effect=HTTPError)
    #     cls.get_patcher.start()

    # @classmethod
    # def tearDownClass(cls):
        # """ tearDownClass method """
        # cls.get_patcher.stop()
