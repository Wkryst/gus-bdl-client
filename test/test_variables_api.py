# coding: utf-8

"""
    BDL API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.variables_api import VariablesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVariablesApi(unittest.TestCase):
    """VariablesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.variables_api.VariablesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_variables_by_id_get(self):
        """Test case for variables_by_id_get

        Zmienna o zadanym Id / Variable with selected Id  # noqa: E501
        """
        pass

    def test_variables_get(self):
        """Test case for variables_get

        Lista zmiennych / Variables list  # noqa: E501
        """
        pass

    def test_variables_metadata_get(self):
        """Test case for variables_metadata_get

        Metadane / Metadata  # noqa: E501
        """
        pass

    def test_variables_search_get(self):
        """Test case for variables_search_get

        Wyszukiwanie zmiennych wg warunków/ Search variables with condition  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
