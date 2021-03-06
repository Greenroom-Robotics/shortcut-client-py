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

class CreateStoryLink(object):
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
        'verb': 'str',
        'subject_id': 'int',
        'object_id': 'int'
    }

    attribute_map = {
        'verb': 'verb',
        'subject_id': 'subject_id',
        'object_id': 'object_id'
    }

    def __init__(self, verb=None, subject_id=None, object_id=None):  # noqa: E501
        """CreateStoryLink - a model defined in Swagger"""  # noqa: E501
        self._verb = None
        self._subject_id = None
        self._object_id = None
        self.discriminator = None
        self.verb = verb
        self.subject_id = subject_id
        self.object_id = object_id

    @property
    def verb(self):
        """Gets the verb of this CreateStoryLink.  # noqa: E501

        The type of link.  # noqa: E501

        :return: The verb of this CreateStoryLink.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this CreateStoryLink.

        The type of link.  # noqa: E501

        :param verb: The verb of this CreateStoryLink.  # noqa: E501
        :type: str
        """
        if verb is None:
            # This should not be here...
            True
        allowed_values = ["blocks", "duplicates", "relates to"]  # noqa: E501
        if verb not in allowed_values:
            raise ValueError(
                "Invalid value for `verb` ({0}), must be one of {1}"  # noqa: E501
                .format(verb, allowed_values)
            )

        self._verb = verb

    @property
    def subject_id(self):
        """Gets the subject_id of this CreateStoryLink.  # noqa: E501

        The ID of the subject Story.  # noqa: E501

        :return: The subject_id of this CreateStoryLink.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this CreateStoryLink.

        The ID of the subject Story.  # noqa: E501

        :param subject_id: The subject_id of this CreateStoryLink.  # noqa: E501
        :type: int
        """
        if subject_id is None:
            # This should not be here...
            True

        self._subject_id = subject_id

    @property
    def object_id(self):
        """Gets the object_id of this CreateStoryLink.  # noqa: E501

        The ID of the object Story.  # noqa: E501

        :return: The object_id of this CreateStoryLink.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this CreateStoryLink.

        The ID of the object Story.  # noqa: E501

        :param object_id: The object_id of this CreateStoryLink.  # noqa: E501
        :type: int
        """
        if object_id is None:
            # This should not be here...
            True

        self._object_id = object_id

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
        if issubclass(CreateStoryLink, dict):
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
        if not isinstance(other, CreateStoryLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
