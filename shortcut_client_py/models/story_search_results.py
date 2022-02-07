# coding: utf-8

"""
    Shortcut API

    Shortcut API  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StorySearchResults(object):
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
        'total': 'int',
        'data': 'list[Story]',
        'next': 'str',
        'cursors': 'list[str]'
    }

    attribute_map = {
        'total': 'total',
        'data': 'data',
        'next': 'next',
        'cursors': 'cursors'
    }

    def __init__(self, total=None, data=None, next=None, cursors=None):  # noqa: E501
        """StorySearchResults - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._data = None
        self._next = None
        self._cursors = None
        self.discriminator = None
        self.total = total
        self.data = data
        self.next = next
        if cursors is not None:
            self.cursors = cursors

    @property
    def total(self):
        """Gets the total of this StorySearchResults.  # noqa: E501

        The total number of matches for the search query. The first 1000 matches can be paged through via the API.  # noqa: E501

        :return: The total of this StorySearchResults.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this StorySearchResults.

        The total number of matches for the search query. The first 1000 matches can be paged through via the API.  # noqa: E501

        :param total: The total of this StorySearchResults.  # noqa: E501
        :type: int
        """
        if total is None:
            # This should not be here...
            True

        self._total = total

    @property
    def data(self):
        """Gets the data of this StorySearchResults.  # noqa: E501

        A list of search results.  # noqa: E501

        :return: The data of this StorySearchResults.  # noqa: E501
        :rtype: list[Story]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this StorySearchResults.

        A list of search results.  # noqa: E501

        :param data: The data of this StorySearchResults.  # noqa: E501
        :type: list[Story]
        """
        if data is None:
            # This should not be here...
            True

        self._data = data

    @property
    def next(self):
        """Gets the next of this StorySearchResults.  # noqa: E501

        The URL path and query string for the next page of search results.  # noqa: E501

        :return: The next of this StorySearchResults.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this StorySearchResults.

        The URL path and query string for the next page of search results.  # noqa: E501

        :param next: The next of this StorySearchResults.  # noqa: E501
        :type: str
        """
        if next is None:
            # This should not be here...
            True

        self._next = next

    @property
    def cursors(self):
        """Gets the cursors of this StorySearchResults.  # noqa: E501


        :return: The cursors of this StorySearchResults.  # noqa: E501
        :rtype: list[str]
        """
        return self._cursors

    @cursors.setter
    def cursors(self, cursors):
        """Sets the cursors of this StorySearchResults.


        :param cursors: The cursors of this StorySearchResults.  # noqa: E501
        :type: list[str]
        """

        self._cursors = cursors

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
        if issubclass(StorySearchResults, dict):
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
        if not isinstance(other, StorySearchResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
