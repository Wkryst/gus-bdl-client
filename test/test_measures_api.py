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
from swagger_client.api.measures_api import MeasuresApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMeasuresApi(unittest.TestCase):
    """MeasuresApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.measures_api.MeasuresApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_measures_by_id_get(self):
        """Test case for measures_by_id_get

        Jednostka miary o zadanym Id / Measure unit with selected Id  # noqa: E501
        """
        pass

    def test_measures_get(self):
        """Test case for measures_get

        Lista jednostek miary / Measure units list  # noqa: E501
        """
        pass

    def test_measures_metadata_get(self):
        """Test case for measures_metadata_get

        Metadane / Metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()