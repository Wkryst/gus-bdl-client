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


class Year(object):
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
        'id': 'int',
        'has_localities': 'bool',
        'quarterly': 'str'
    }

    attribute_map = {
        'id': 'id',
        'has_localities': 'hasLocalities',
        'quarterly': 'quarterly'
    }

    def __init__(self, id=None, has_localities=None, quarterly=None):  # noqa: E501
        """Year - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._has_localities = None
        self._quarterly = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if has_localities is not None:
            self.has_localities = has_localities
        if quarterly is not None:
            self.quarterly = quarterly

    @property
    def id(self):
        """Gets the id of this Year.  # noqa: E501

        Identyfikator roku / Year identifier  # noqa: E501

        :return: The id of this Year.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Year.

        Identyfikator roku / Year identifier  # noqa: E501

        :param id: The id of this Year.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def has_localities(self):
        """Gets the has_localities of this Year.  # noqa: E501

        Czy są miejscowości? / Are localities in this year?  # noqa: E501

        :return: The has_localities of this Year.  # noqa: E501
        :rtype: bool
        """
        return self._has_localities

    @has_localities.setter
    def has_localities(self, has_localities):
        """Sets the has_localities of this Year.

        Czy są miejscowości? / Are localities in this year?  # noqa: E501

        :param has_localities: The has_localities of this Year.  # noqa: E501
        :type: bool
        """

        self._has_localities = has_localities

    @property
    def quarterly(self):
        """Gets the quarterly of this Year.  # noqa: E501

        Dane roczne lub kwartalne / Yearly or quarterly data  # noqa: E501

        :return: The quarterly of this Year.  # noqa: E501
        :rtype: str
        """
        return self._quarterly

    @quarterly.setter
    def quarterly(self, quarterly):
        """Sets the quarterly of this Year.

        Dane roczne lub kwartalne / Yearly or quarterly data  # noqa: E501

        :param quarterly: The quarterly of this Year.  # noqa: E501
        :type: str
        """

        self._quarterly = quarterly

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
        if issubclass(Year, dict):
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
        if not isinstance(other, Year):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
