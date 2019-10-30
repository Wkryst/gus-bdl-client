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


class PageLinks(object):
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
        'first': 'str',
        'prev': 'str',
        '_self': 'str',
        'next': 'str',
        'last': 'str'
    }

    attribute_map = {
        'first': 'first',
        'prev': 'prev',
        '_self': 'self',
        'next': 'next',
        'last': 'last'
    }

    def __init__(self, first=None, prev=None, _self=None, next=None, last=None):  # noqa: E501
        """PageLinks - a model defined in Swagger"""  # noqa: E501

        self._first = None
        self._prev = None
        self.__self = None
        self._next = None
        self._last = None
        self.discriminator = None

        if first is not None:
            self.first = first
        if prev is not None:
            self.prev = prev
        if _self is not None:
            self._self = _self
        if next is not None:
            self.next = next
        if last is not None:
            self.last = last

    @property
    def first(self):
        """Gets the first of this PageLinks.  # noqa: E501

        Pierwsza strona / First page  # noqa: E501

        :return: The first of this PageLinks.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this PageLinks.

        Pierwsza strona / First page  # noqa: E501

        :param first: The first of this PageLinks.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def prev(self):
        """Gets the prev of this PageLinks.  # noqa: E501

        Poprzednia strona / Previous page  # noqa: E501

        :return: The prev of this PageLinks.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this PageLinks.

        Poprzednia strona / Previous page  # noqa: E501

        :param prev: The prev of this PageLinks.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def _self(self):
        """Gets the _self of this PageLinks.  # noqa: E501

        Bieżąca strona / Current page  # noqa: E501

        :return: The _self of this PageLinks.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this PageLinks.

        Bieżąca strona / Current page  # noqa: E501

        :param _self: The _self of this PageLinks.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def next(self):
        """Gets the next of this PageLinks.  # noqa: E501

        Następna strona / Next page  # noqa: E501

        :return: The next of this PageLinks.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PageLinks.

        Następna strona / Next page  # noqa: E501

        :param next: The next of this PageLinks.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def last(self):
        """Gets the last of this PageLinks.  # noqa: E501

        Ostatnia strona / Last page  # noqa: E501

        :return: The last of this PageLinks.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this PageLinks.

        Ostatnia strona / Last page  # noqa: E501

        :param last: The last of this PageLinks.  # noqa: E501
        :type: str
        """

        self._last = last

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
        if issubclass(PageLinks, dict):
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
        if not isinstance(other, PageLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
