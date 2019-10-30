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


class ErrorMessage(object):
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
        'error_result': 'str',
        'error_reason': 'str',
        'error_solution': 'str',
        'error_code': 'int',
        'error_help': 'str'
    }

    attribute_map = {
        'error_result': 'errorResult',
        'error_reason': 'errorReason',
        'error_solution': 'errorSolution',
        'error_code': 'errorCode',
        'error_help': 'errorHelp'
    }

    def __init__(self, error_result=None, error_reason=None, error_solution=None, error_code=None, error_help=None):  # noqa: E501
        """ErrorMessage - a model defined in Swagger"""  # noqa: E501

        self._error_result = None
        self._error_reason = None
        self._error_solution = None
        self._error_code = None
        self._error_help = None
        self.discriminator = None

        if error_result is not None:
            self.error_result = error_result
        if error_reason is not None:
            self.error_reason = error_reason
        if error_solution is not None:
            self.error_solution = error_solution
        if error_code is not None:
            self.error_code = error_code
        if error_help is not None:
            self.error_help = error_help

    @property
    def error_result(self):
        """Gets the error_result of this ErrorMessage.  # noqa: E501

        Opis błędu / Error result  # noqa: E501

        :return: The error_result of this ErrorMessage.  # noqa: E501
        :rtype: str
        """
        return self._error_result

    @error_result.setter
    def error_result(self, error_result):
        """Sets the error_result of this ErrorMessage.

        Opis błędu / Error result  # noqa: E501

        :param error_result: The error_result of this ErrorMessage.  # noqa: E501
        :type: str
        """

        self._error_result = error_result

    @property
    def error_reason(self):
        """Gets the error_reason of this ErrorMessage.  # noqa: E501

        Opis przyczyny błędu / Error reason description  # noqa: E501

        :return: The error_reason of this ErrorMessage.  # noqa: E501
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        """Sets the error_reason of this ErrorMessage.

        Opis przyczyny błędu / Error reason description  # noqa: E501

        :param error_reason: The error_reason of this ErrorMessage.  # noqa: E501
        :type: str
        """

        self._error_reason = error_reason

    @property
    def error_solution(self):
        """Gets the error_solution of this ErrorMessage.  # noqa: E501

        Rozwiązanie problemu / Error solution  # noqa: E501

        :return: The error_solution of this ErrorMessage.  # noqa: E501
        :rtype: str
        """
        return self._error_solution

    @error_solution.setter
    def error_solution(self, error_solution):
        """Sets the error_solution of this ErrorMessage.

        Rozwiązanie problemu / Error solution  # noqa: E501

        :param error_solution: The error_solution of this ErrorMessage.  # noqa: E501
        :type: str
        """

        self._error_solution = error_solution

    @property
    def error_code(self):
        """Gets the error_code of this ErrorMessage.  # noqa: E501

        Kod błędu / Error code  # noqa: E501

        :return: The error_code of this ErrorMessage.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ErrorMessage.

        Kod błędu / Error code  # noqa: E501

        :param error_code: The error_code of this ErrorMessage.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def error_help(self):
        """Gets the error_help of this ErrorMessage.  # noqa: E501

        Link do pomocy / Help link  # noqa: E501

        :return: The error_help of this ErrorMessage.  # noqa: E501
        :rtype: str
        """
        return self._error_help

    @error_help.setter
    def error_help(self, error_help):
        """Sets the error_help of this ErrorMessage.

        Link do pomocy / Help link  # noqa: E501

        :param error_help: The error_help of this ErrorMessage.  # noqa: E501
        :type: str
        """

        self._error_help = error_help

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
        if issubclass(ErrorMessage, dict):
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
        if not isinstance(other, ErrorMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
