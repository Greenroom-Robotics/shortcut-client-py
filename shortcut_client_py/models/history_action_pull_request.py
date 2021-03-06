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

class HistoryActionPullRequest(object):
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
        'entity_type': 'str',
        'action': 'str',
        'number': 'int',
        'title': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entity_type',
        'action': 'action',
        'number': 'number',
        'title': 'title',
        'url': 'url'
    }

    def __init__(self, id=None, entity_type=None, action=None, number=None, title=None, url=None):  # noqa: E501
        """HistoryActionPullRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity_type = None
        self._action = None
        self._number = None
        self._title = None
        self._url = None
        self.discriminator = None
        self.id = id
        self.entity_type = entity_type
        self.action = action
        self.number = number
        self.title = title
        self.url = url

    @property
    def id(self):
        """Gets the id of this HistoryActionPullRequest.  # noqa: E501

        The ID of the entity referenced.  # noqa: E501

        :return: The id of this HistoryActionPullRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryActionPullRequest.

        The ID of the entity referenced.  # noqa: E501

        :param id: The id of this HistoryActionPullRequest.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this HistoryActionPullRequest.  # noqa: E501

        The type of entity referenced.  # noqa: E501

        :return: The entity_type of this HistoryActionPullRequest.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this HistoryActionPullRequest.

        The type of entity referenced.  # noqa: E501

        :param entity_type: The entity_type of this HistoryActionPullRequest.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def action(self):
        """Gets the action of this HistoryActionPullRequest.  # noqa: E501

        The action of the entity referenced.  # noqa: E501

        :return: The action of this HistoryActionPullRequest.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HistoryActionPullRequest.

        The action of the entity referenced.  # noqa: E501

        :param action: The action of this HistoryActionPullRequest.  # noqa: E501
        :type: str
        """
        if action is None:
            # This should not be here...
            True
        allowed_values = ["open", "update", "reopen", "close", "sync", "comment"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def number(self):
        """Gets the number of this HistoryActionPullRequest.  # noqa: E501

        The VCS Repository-specific ID for the Pull Request.  # noqa: E501

        :return: The number of this HistoryActionPullRequest.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this HistoryActionPullRequest.

        The VCS Repository-specific ID for the Pull Request.  # noqa: E501

        :param number: The number of this HistoryActionPullRequest.  # noqa: E501
        :type: int
        """
        if number is None:
            # This should not be here...
            True

        self._number = number

    @property
    def title(self):
        """Gets the title of this HistoryActionPullRequest.  # noqa: E501

        The title of the Pull Request.  # noqa: E501

        :return: The title of this HistoryActionPullRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this HistoryActionPullRequest.

        The title of the Pull Request.  # noqa: E501

        :param title: The title of this HistoryActionPullRequest.  # noqa: E501
        :type: str
        """
        if title is None:
            # This should not be here...
            True

        self._title = title

    @property
    def url(self):
        """Gets the url of this HistoryActionPullRequest.  # noqa: E501

        The URL from the provider of the VCS Pull Request.  # noqa: E501

        :return: The url of this HistoryActionPullRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HistoryActionPullRequest.

        The URL from the provider of the VCS Pull Request.  # noqa: E501

        :param url: The url of this HistoryActionPullRequest.  # noqa: E501
        :type: str
        """
        if url is None:
            # This should not be here...
            True

        self._url = url

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
        if issubclass(HistoryActionPullRequest, dict):
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
        if not isinstance(other, HistoryActionPullRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
