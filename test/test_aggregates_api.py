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
from swagger_client.api.aggregates_api import AggregatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAggregatesApi(unittest.TestCase):
    """AggregatesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.aggregates_api.AggregatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aggregates_by_id_get(self):
        """Test case for aggregates_by_id_get

        Poziom agregacji o zadanym Id / Aggregation level with selected Id  # noqa: E501
        """
        pass

    def test_aggregates_get(self):
        """Test case for aggregates_get

        Lista poziomów agregacji / Aggregation level list  # noqa: E501
        """
        pass

    def test_aggregates_metadata_get(self):
        """Test case for aggregates_metadata_get

        Metadane / Metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()