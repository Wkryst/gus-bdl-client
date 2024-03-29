# coding: utf-8

"""
    BDL API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SingleVariableData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total_records': 'int',
        'page': 'int',
        'page_size': 'int',
        'links': 'PageLinks',
        'variable_id': 'int',
        'measure_unit_id': 'int',
        'aggregate_id': 'int',
        'last_update': 'datetime',
        'results': 'list[UnitData]'
    }

    attribute_map = {
        'total_records': 'totalRecords',
        'page': 'page',
        'page_size': 'pageSize',
        'links': 'links',
        'variable_id': 'variableId',
        'measure_unit_id': 'measureUnitId',
        'aggregate_id': 'aggregateId',
        'last_update': 'lastUpdate',
        'results': 'results'
    }

    def __init__(self, total_records=None, page=None, page_size=None, links=None, variable_id=None, measure_unit_id=None, aggregate_id=None, last_update=None, results=None):  # noqa: E501
        """SingleVariableData - a model defined in Swagger"""  # noqa: E501

        self._total_records = None
        self._page = None
        self._page_size = None
        self._links = None
        self._variable_id = None
        self._measure_unit_id = None
        self._aggregate_id = None
        self._last_update = None
        self._results = None
        self.discriminator = None

        if total_records is not None:
            self.total_records = total_records
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if links is not None:
            self.links = links
        if variable_id is not None:
            self.variable_id = variable_id
        if measure_unit_id is not None:
            self.measure_unit_id = measure_unit_id
        if aggregate_id is not None:
            self.aggregate_id = aggregate_id
        if last_update is not None:
            self.last_update = last_update
        if results is not None:
            self.results = results

    @property
    def total_records(self):
        """Gets the total_records of this SingleVariableData.  # noqa: E501

          # noqa: E501

        :return: The total_records of this SingleVariableData.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this SingleVariableData.

          # noqa: E501

        :param total_records: The total_records of this SingleVariableData.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def page(self):
        """Gets the page of this SingleVariableData.  # noqa: E501

          # noqa: E501

        :return: The page of this SingleVariableData.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SingleVariableData.

          # noqa: E501

        :param page: The page of this SingleVariableData.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this SingleVariableData.  # noqa: E501

          # noqa: E501

        :return: The page_size of this SingleVariableData.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SingleVariableData.

          # noqa: E501

        :param page_size: The page_size of this SingleVariableData.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def links(self):
        """Gets the links of this SingleVariableData.  # noqa: E501


        :return: The links of this SingleVariableData.  # noqa: E501
        :rtype: PageLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SingleVariableData.


        :param links: The links of this SingleVariableData.  # noqa: E501
        :type: PageLinks
        """

        self._links = links

    @property
    def variable_id(self):
        """Gets the variable_id of this SingleVariableData.  # noqa: E501

        Identyfikator zmiennej / Variable's identifier  # noqa: E501

        :return: The variable_id of this SingleVariableData.  # noqa: E501
        :rtype: int
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id):
        """Sets the variable_id of this SingleVariableData.

        Identyfikator zmiennej / Variable's identifier  # noqa: E501

        :param variable_id: The variable_id of this SingleVariableData.  # noqa: E501
        :type: int
        """

        self._variable_id = variable_id

    @property
    def measure_unit_id(self):
        """Gets the measure_unit_id of this SingleVariableData.  # noqa: E501

        Identyfikator jednostki miary / Measure unit's identifier  # noqa: E501

        :return: The measure_unit_id of this SingleVariableData.  # noqa: E501
        :rtype: int
        """
        return self._measure_unit_id

    @measure_unit_id.setter
    def measure_unit_id(self, measure_unit_id):
        """Sets the measure_unit_id of this SingleVariableData.

        Identyfikator jednostki miary / Measure unit's identifier  # noqa: E501

        :param measure_unit_id: The measure_unit_id of this SingleVariableData.  # noqa: E501
        :type: int
        """

        self._measure_unit_id = measure_unit_id

    @property
    def aggregate_id(self):
        """Gets the aggregate_id of this SingleVariableData.  # noqa: E501

        Identyfikator agregatu / Aggregate's identifier  # noqa: E501

        :return: The aggregate_id of this SingleVariableData.  # noqa: E501
        :rtype: int
        """
        return self._aggregate_id

    @aggregate_id.setter
    def aggregate_id(self, aggregate_id):
        """Sets the aggregate_id of this SingleVariableData.

        Identyfikator agregatu / Aggregate's identifier  # noqa: E501

        :param aggregate_id: The aggregate_id of this SingleVariableData.  # noqa: E501
        :type: int
        """

        self._aggregate_id = aggregate_id

    @property
    def last_update(self):
        """Gets the last_update of this SingleVariableData.  # noqa: E501

        Data ostatniej modyfikacji / Last update  # noqa: E501

        :return: The last_update of this SingleVariableData.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this SingleVariableData.

        Data ostatniej modyfikacji / Last update  # noqa: E501

        :param last_update: The last_update of this SingleVariableData.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def results(self):
        """Gets the results of this SingleVariableData.  # noqa: E501

        Wartości dla jednostek / Values for units  # noqa: E501

        :return: The results of this SingleVariableData.  # noqa: E501
        :rtype: list[UnitData]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this SingleVariableData.

        Wartości dla jednostek / Values for units  # noqa: E501

        :param results: The results of this SingleVariableData.  # noqa: E501
        :type: list[UnitData]
        """

        self._results = results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SingleVariableData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SingleVariableData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
