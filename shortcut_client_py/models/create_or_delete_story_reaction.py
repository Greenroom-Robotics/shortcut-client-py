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

class CreateOrDeleteStoryReaction(object):
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
        'emoji': 'str'
    }

    attribute_map = {
        'emoji': 'emoji'
    }

    def __init__(self, emoji=None):  # noqa: E501
        """CreateOrDeleteStoryReaction - a model defined in Swagger"""  # noqa: E501
        self._emoji = None
        self.discriminator = None
        self.emoji = emoji

    @property
    def emoji(self):
        """Gets the emoji of this CreateOrDeleteStoryReaction.  # noqa: E501

        The emoji short-code to add / remove. E.g. `:thumbsup::skin-tone-4:`.  # noqa: E501

        :return: The emoji of this CreateOrDeleteStoryReaction.  # noqa: E501
        :rtype: str
        """
        return self._emoji

    @emoji.setter
    def emoji(self, emoji):
        """Sets the emoji of this CreateOrDeleteStoryReaction.

        The emoji short-code to add / remove. E.g. `:thumbsup::skin-tone-4:`.  # noqa: E501

        :param emoji: The emoji of this CreateOrDeleteStoryReaction.  # noqa: E501
        :type: str
        """
        if emoji is None:
            # This should not be here...
            True

        self._emoji = emoji

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
        if issubclass(CreateOrDeleteStoryReaction, dict):
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
        if not isinstance(other, CreateOrDeleteStoryReaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
