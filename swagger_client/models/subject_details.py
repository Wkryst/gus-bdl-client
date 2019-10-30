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


class SubjectDetails(object):
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
        'id': 'str',
        'parent_id': 'str',
        'name': 'str',
        'has_variables': 'bool',
        'children': 'list[str]',
        'years': 'list[int]',
        'levels': 'list[int]',
        'availability': 'list[Available]',
        'dimensions': 'list[str]',
        'last_update': 'datetime',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parentId',
        'name': 'name',
        'has_variables': 'hasVariables',
        'children': 'children',
        'years': 'years',
        'levels': 'levels',
        'availability': 'availability',
        'dimensions': 'dimensions',
        'last_update': 'lastUpdate',
        'description': 'description'
    }

    def __init__(self, id=None, parent_id=None, name=None, has_variables=None, children=None, years=None, levels=None, availability=None, dimensions=None, last_update=None, description=None):  # noqa: E501
        """SubjectDetails - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_id = None
        self._name = None
        self._has_variables = None
        self._children = None
        self._years = None
        self._levels = None
        self._availability = None
        self._dimensions = None
        self._last_update = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if has_variables is not None:
            self.has_variables = has_variables
        if children is not None:
            self.children = children
        if years is not None:
            self.years = years
        if levels is not None:
            self.levels = levels
        if availability is not None:
            self.availability = availability
        if dimensions is not None:
            self.dimensions = dimensions
        if last_update is not None:
            self.last_update = last_update
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this SubjectDetails.  # noqa: E501

        Identyfikator tematu / Subject identifier  # noqa: E501

        :return: The id of this SubjectDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubjectDetails.

        Identyfikator tematu / Subject identifier  # noqa: E501

        :param id: The id of this SubjectDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this SubjectDetails.  # noqa: E501

        Identyfikator tematu nadrzędnego / Parent subject identifier  # noqa: E501

        :return: The parent_id of this SubjectDetails.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this SubjectDetails.

        Identyfikator tematu nadrzędnego / Parent subject identifier  # noqa: E501

        :param parent_id: The parent_id of this SubjectDetails.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this SubjectDetails.  # noqa: E501

        Nazwa tematu / Subject name  # noqa: E501

        :return: The name of this SubjectDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubjectDetails.

        Nazwa tematu / Subject name  # noqa: E501

        :param name: The name of this SubjectDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def has_variables(self):
        """Gets the has_variables of this SubjectDetails.  # noqa: E501

        Czy temat posiada zmienne / Does the subject has variables  # noqa: E501

        :return: The has_variables of this SubjectDetails.  # noqa: E501
        :rtype: bool
        """
        return self._has_variables

    @has_variables.setter
    def has_variables(self, has_variables):
        """Sets the has_variables of this SubjectDetails.

        Czy temat posiada zmienne / Does the subject has variables  # noqa: E501

        :param has_variables: The has_variables of this SubjectDetails.  # noqa: E501
        :type: bool
        """

        self._has_variables = has_variables

    @property
    def children(self):
        """Gets the children of this SubjectDetails.  # noqa: E501

        Identyfikatory tematów podrzędnych / Children subject identifiers  # noqa: E501

        :return: The children of this SubjectDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this SubjectDetails.

        Identyfikatory tematów podrzędnych / Children subject identifiers  # noqa: E501

        :param children: The children of this SubjectDetails.  # noqa: E501
        :type: list[str]
        """

        self._children = children

    @property
    def years(self):
        """Gets the years of this SubjectDetails.  # noqa: E501

        Lata obowiązywania tematu / Years of subject validity  # noqa: E501

        :return: The years of this SubjectDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this SubjectDetails.

        Lata obowiązywania tematu / Years of subject validity  # noqa: E501

        :param years: The years of this SubjectDetails.  # noqa: E501
        :type: list[int]
        """

        self._years = years

    @property
    def levels(self):
        """Gets the levels of this SubjectDetails.  # noqa: E501

        Poziomy agregacji tematu / Subject agregate levels  # noqa: E501

        :return: The levels of this SubjectDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this SubjectDetails.

        Poziomy agregacji tematu / Subject agregate levels  # noqa: E501

        :param levels: The levels of this SubjectDetails.  # noqa: E501
        :type: list[int]
        """

        self._levels = levels

    @property
    def availability(self):
        """Gets the availability of this SubjectDetails.  # noqa: E501

        Opis dostępności w latach / Description of availability in years  # noqa: E501

        :return: The availability of this SubjectDetails.  # noqa: E501
        :rtype: list[Available]
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this SubjectDetails.

        Opis dostępności w latach / Description of availability in years  # noqa: E501

        :param availability: The availability of this SubjectDetails.  # noqa: E501
        :type: list[Available]
        """

        self._availability = availability

    @property
    def dimensions(self):
        """Gets the dimensions of this SubjectDetails.  # noqa: E501

        Wymiary tematu / Subject dimensions  # noqa: E501

        :return: The dimensions of this SubjectDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this SubjectDetails.

        Wymiary tematu / Subject dimensions  # noqa: E501

        :param dimensions: The dimensions of this SubjectDetails.  # noqa: E501
        :type: list[str]
        """

        self._dimensions = dimensions

    @property
    def last_update(self):
        """Gets the last_update of this SubjectDetails.  # noqa: E501

        Data ostatniej aktualizacji tematu / Date of the last update of the subject  # noqa: E501

        :return: The last_update of this SubjectDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this SubjectDetails.

        Data ostatniej aktualizacji tematu / Date of the last update of the subject  # noqa: E501

        :param last_update: The last_update of this SubjectDetails.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def description(self):
        """Gets the description of this SubjectDetails.  # noqa: E501

        Opis tematu / Subject description  # noqa: E501

        :return: The description of this SubjectDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubjectDetails.

        Opis tematu / Subject description  # noqa: E501

        :param description: The description of this SubjectDetails.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(SubjectDetails, dict):
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
        if not isinstance(other, SubjectDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
