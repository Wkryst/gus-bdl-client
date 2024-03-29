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
from swagger_client.api.levels_api import LevelsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLevelsApi(unittest.TestCase):
    """LevelsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.levels_api.LevelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_levels_by_id_get(self):
        """Test case for levels_by_id_get

        Poziom obowiązywania o zadanym Id / Availability level with selected Id  # noqa: E501
        """
        pass

    def test_levels_get(self):
        """Test case for levels_get

        Lista poziomów obowiązywania / Availability levels list  # noqa: E501
        """
        pass

    def test_levels_metadata_get(self):
        """Test case for levels_metadata_get

        Metadane / Metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
