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

class HistoryActionStoryCommentCreate(object):
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
        'app_url': 'str',
        'text': 'str',
        'author_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entity_type',
        'action': 'action',
        'app_url': 'app_url',
        'text': 'text',
        'author_id': 'author_id'
    }

    def __init__(self, id=None, entity_type=None, action=None, app_url=None, text=None, author_id=None):  # noqa: E501
        """HistoryActionStoryCommentCreate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity_type = None
        self._action = None
        self._app_url = None
        self._text = None
        self._author_id = None
        self.discriminator = None
        self.id = id
        self.entity_type = entity_type
        self.action = action
        self.app_url = app_url
        self.text = text
        self.author_id = author_id

    @property
    def id(self):
        """Gets the id of this HistoryActionStoryCommentCreate.  # noqa: E501

        The ID of the entity referenced.  # noqa: E501

        :return: The id of this HistoryActionStoryCommentCreate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryActionStoryCommentCreate.

        The ID of the entity referenced.  # noqa: E501

        :param id: The id of this HistoryActionStoryCommentCreate.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this HistoryActionStoryCommentCreate.  # noqa: E501

        The type of entity referenced.  # noqa: E501

        :return: The entity_type of this HistoryActionStoryCommentCreate.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this HistoryActionStoryCommentCreate.

        The type of entity referenced.  # noqa: E501

        :param entity_type: The entity_type of this HistoryActionStoryCommentCreate.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def action(self):
        """Gets the action of this HistoryActionStoryCommentCreate.  # noqa: E501

        The action of the entity referenced.  # noqa: E501

        :return: The action of this HistoryActionStoryCommentCreate.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HistoryActionStoryCommentCreate.

        The action of the entity referenced.  # noqa: E501

        :param action: The action of this HistoryActionStoryCommentCreate.  # noqa: E501
        :type: str
        """
        if action is None:
            # This should not be here...
            True
        allowed_values = ["create"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def app_url(self):
        """Gets the app_url of this HistoryActionStoryCommentCreate.  # noqa: E501

        The application URL of the Story Comment.  # noqa: E501

        :return: The app_url of this HistoryActionStoryCommentCreate.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this HistoryActionStoryCommentCreate.

        The application URL of the Story Comment.  # noqa: E501

        :param app_url: The app_url of this HistoryActionStoryCommentCreate.  # noqa: E501
        :type: str
        """
        if app_url is None:
            # This should not be here...
            True

        self._app_url = app_url

    @property
    def text(self):
        """Gets the text of this HistoryActionStoryCommentCreate.  # noqa: E501

        The text of the Story Comment.  # noqa: E501

        :return: The text of this HistoryActionStoryCommentCreate.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this HistoryActionStoryCommentCreate.

        The text of the Story Comment.  # noqa: E501

        :param text: The text of this HistoryActionStoryCommentCreate.  # noqa: E501
        :type: str
        """
        if text is None:
            # This should not be here...
            True

        self._text = text

    @property
    def author_id(self):
        """Gets the author_id of this HistoryActionStoryCommentCreate.  # noqa: E501

        The Member ID of who created the Story Comment.  # noqa: E501

        :return: The author_id of this HistoryActionStoryCommentCreate.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this HistoryActionStoryCommentCreate.

        The Member ID of who created the Story Comment.  # noqa: E501

        :param author_id: The author_id of this HistoryActionStoryCommentCreate.  # noqa: E501
        :type: str
        """
        if author_id is None:
            # This should not be here...
            True

        self._author_id = author_id

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
        if issubclass(HistoryActionStoryCommentCreate, dict):
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
        if not isinstance(other, HistoryActionStoryCommentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
