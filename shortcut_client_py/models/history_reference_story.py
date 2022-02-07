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

class HistoryReferenceStory(object):
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
        'app_url': 'str',
        'name': 'str',
        'story_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entity_type',
        'app_url': 'app_url',
        'name': 'name',
        'story_type': 'story_type'
    }

    def __init__(self, id=None, entity_type=None, app_url=None, name=None, story_type=None):  # noqa: E501
        """HistoryReferenceStory - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity_type = None
        self._app_url = None
        self._name = None
        self._story_type = None
        self.discriminator = None
        self.id = id
        self.entity_type = entity_type
        self.app_url = app_url
        self.name = name
        self.story_type = story_type

    @property
    def id(self):
        """Gets the id of this HistoryReferenceStory.  # noqa: E501

        The ID of the entity referenced.  # noqa: E501

        :return: The id of this HistoryReferenceStory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryReferenceStory.

        The ID of the entity referenced.  # noqa: E501

        :param id: The id of this HistoryReferenceStory.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this HistoryReferenceStory.  # noqa: E501

        The type of entity referenced.  # noqa: E501

        :return: The entity_type of this HistoryReferenceStory.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this HistoryReferenceStory.

        The type of entity referenced.  # noqa: E501

        :param entity_type: The entity_type of this HistoryReferenceStory.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def app_url(self):
        """Gets the app_url of this HistoryReferenceStory.  # noqa: E501

        The application URL of the Story.  # noqa: E501

        :return: The app_url of this HistoryReferenceStory.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this HistoryReferenceStory.

        The application URL of the Story.  # noqa: E501

        :param app_url: The app_url of this HistoryReferenceStory.  # noqa: E501
        :type: str
        """
        if app_url is None:
            # This should not be here...
            True

        self._app_url = app_url

    @property
    def name(self):
        """Gets the name of this HistoryReferenceStory.  # noqa: E501

        The name of the entity referenced.  # noqa: E501

        :return: The name of this HistoryReferenceStory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HistoryReferenceStory.

        The name of the entity referenced.  # noqa: E501

        :param name: The name of this HistoryReferenceStory.  # noqa: E501
        :type: str
        """
        if name is None:
            # This should not be here...
            True

        self._name = name

    @property
    def story_type(self):
        """Gets the story_type of this HistoryReferenceStory.  # noqa: E501

        If the referenced entity is a Story, either \"bug\", \"chore\", or \"feature\".  # noqa: E501

        :return: The story_type of this HistoryReferenceStory.  # noqa: E501
        :rtype: str
        """
        return self._story_type

    @story_type.setter
    def story_type(self, story_type):
        """Sets the story_type of this HistoryReferenceStory.

        If the referenced entity is a Story, either \"bug\", \"chore\", or \"feature\".  # noqa: E501

        :param story_type: The story_type of this HistoryReferenceStory.  # noqa: E501
        :type: str
        """
        if story_type is None:
            # This should not be here...
            True
        allowed_values = ["feature", "chore", "bug"]  # noqa: E501
        if story_type not in allowed_values:
            raise ValueError(
                "Invalid value for `story_type` ({0}), must be one of {1}"  # noqa: E501
                .format(story_type, allowed_values)
            )

        self._story_type = story_type

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
        if issubclass(HistoryReferenceStory, dict):
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
        if not isinstance(other, HistoryReferenceStory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
