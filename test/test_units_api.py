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
from swagger_client.api.units_api import UnitsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUnitsApi(unittest.TestCase):
    """UnitsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.units_api.UnitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_units_by_id_get(self):
        """Test case for units_by_id_get

        Jednostka terytorialna (do poziomu gminy) o zadanym Id / Territorial unit (to gmina level) with selected Id  # noqa: E501
        """
        pass

    def test_units_get(self):
        """Test case for units_get

        Lista jednostek terytorialnych / Territorial units list  # noqa: E501
        """
        pass

    def test_units_localities_by_id_get(self):
        """Test case for units_localities_by_id_get

        Miejscowość statystyczna o zadanym Id / Statistical locality with selected Id  # noqa: E501
        """
        pass

    def test_units_localities_get(self):
        """Test case for units_localities_get

        Lista miejscowości statystycznych / Statistical localities list  # noqa: E501
        """
        pass

    def test_units_localities_search_get(self):
        """Test case for units_localities_search_get

        Wyszukiwanie miejscowości statystycznych wg nazwy / Searching statistical localities by name  # noqa: E501
        """
        pass

    def test_units_metadata_get(self):
        """Test case for units_metadata_get

        Metadane / Metadata  # noqa: E501
        """
        pass

    def test_units_search_get(self):
        """Test case for units_search_get

        Wyszukiwanie jednostek wg nazwy / Searching territorial units by name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()