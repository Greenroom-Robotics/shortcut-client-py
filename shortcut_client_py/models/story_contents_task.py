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

class StoryContentsTask(object):
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
        'description': 'str',
        'position': 'int',
        'complete': 'bool',
        'owner_ids': 'list[str]',
        'external_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'position': 'position',
        'complete': 'complete',
        'owner_ids': 'owner_ids',
        'external_id': 'external_id'
    }

    def __init__(self, description=None, position=None, complete=None, owner_ids=None, external_id=None):  # noqa: E501
        """StoryContentsTask - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._position = None
        self._complete = None
        self._owner_ids = None
        self._external_id = None
        self.discriminator = None
        self.description = description
        if position is not None:
            self.position = position
        if complete is not None:
            self.complete = complete
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if external_id is not None:
            self.external_id = external_id

    @property
    def description(self):
        """Gets the description of this StoryContentsTask.  # noqa: E501

        Full text of the Task.  # noqa: E501

        :return: The description of this StoryContentsTask.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StoryContentsTask.

        Full text of the Task.  # noqa: E501

        :param description: The description of this StoryContentsTask.  # noqa: E501
        :type: str
        """
        if description is None:
            # This should not be here...
            True

        self._description = description

    @property
    def position(self):
        """Gets the position of this StoryContentsTask.  # noqa: E501

        The number corresponding to the Task's position within a list of Tasks on a Story.  # noqa: E501

        :return: The position of this StoryContentsTask.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this StoryContentsTask.

        The number corresponding to the Task's position within a list of Tasks on a Story.  # noqa: E501

        :param position: The position of this StoryContentsTask.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def complete(self):
        """Gets the complete of this StoryContentsTask.  # noqa: E501

        True/false boolean indicating whether the Task has been completed.  # noqa: E501

        :return: The complete of this StoryContentsTask.  # noqa: E501
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this StoryContentsTask.

        True/false boolean indicating whether the Task has been completed.  # noqa: E501

        :param complete: The complete of this StoryContentsTask.  # noqa: E501
        :type: bool
        """

        self._complete = complete

    @property
    def owner_ids(self):
        """Gets the owner_ids of this StoryContentsTask.  # noqa: E501

        An array of UUIDs of the Owners of this Task.  # noqa: E501

        :return: The owner_ids of this StoryContentsTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this StoryContentsTask.

        An array of UUIDs of the Owners of this Task.  # noqa: E501

        :param owner_ids: The owner_ids of this StoryContentsTask.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids = owner_ids

    @property
    def external_id(self):
        """Gets the external_id of this StoryContentsTask.  # noqa: E501

        This field can be set to another unique ID. In the case that the Task has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this StoryContentsTask.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this StoryContentsTask.

        This field can be set to another unique ID. In the case that the Task has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this StoryContentsTask.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(StoryContentsTask, dict):
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
        if not isinstance(other, StoryContentsTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
