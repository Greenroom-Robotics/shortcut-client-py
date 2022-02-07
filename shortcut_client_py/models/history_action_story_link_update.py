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

class HistoryActionStoryLinkUpdate(object):
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
        'verb': 'str',
        'subject_id': 'int',
        'object_id': 'int',
        'changes': 'HistoryChangesStoryLink'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entity_type',
        'action': 'action',
        'verb': 'verb',
        'subject_id': 'subject_id',
        'object_id': 'object_id',
        'changes': 'changes'
    }

    def __init__(self, id=None, entity_type=None, action=None, verb=None, subject_id=None, object_id=None, changes=None):  # noqa: E501
        """HistoryActionStoryLinkUpdate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity_type = None
        self._action = None
        self._verb = None
        self._subject_id = None
        self._object_id = None
        self._changes = None
        self.discriminator = None
        self.id = id
        self.entity_type = entity_type
        self.action = action
        self.verb = verb
        self.subject_id = subject_id
        self.object_id = object_id
        self.changes = changes

    @property
    def id(self):
        """Gets the id of this HistoryActionStoryLinkUpdate.  # noqa: E501

        The ID of the entity referenced.  # noqa: E501

        :return: The id of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryActionStoryLinkUpdate.

        The ID of the entity referenced.  # noqa: E501

        :param id: The id of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this HistoryActionStoryLinkUpdate.  # noqa: E501

        The type of entity referenced.  # noqa: E501

        :return: The entity_type of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this HistoryActionStoryLinkUpdate.

        The type of entity referenced.  # noqa: E501

        :param entity_type: The entity_type of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def action(self):
        """Gets the action of this HistoryActionStoryLinkUpdate.  # noqa: E501

        The action of the entity referenced.  # noqa: E501

        :return: The action of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HistoryActionStoryLinkUpdate.

        The action of the entity referenced.  # noqa: E501

        :param action: The action of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :type: str
        """
        if action is None:
            # This should not be here...
            True
        allowed_values = ["update"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def verb(self):
        """Gets the verb of this HistoryActionStoryLinkUpdate.  # noqa: E501

        The verb describing the link's relationship.  # noqa: E501

        :return: The verb of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this HistoryActionStoryLinkUpdate.

        The verb describing the link's relationship.  # noqa: E501

        :param verb: The verb of this HistoryActionStoryLinkUpdate.  # noqa: E501
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
        """Gets the subject_id of this HistoryActionStoryLinkUpdate.  # noqa: E501

        The Story ID of the subject Story.  # noqa: E501

        :return: The subject_id of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this HistoryActionStoryLinkUpdate.

        The Story ID of the subject Story.  # noqa: E501

        :param subject_id: The subject_id of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :type: int
        """
        if subject_id is None:
            # This should not be here...
            True

        self._subject_id = subject_id

    @property
    def object_id(self):
        """Gets the object_id of this HistoryActionStoryLinkUpdate.  # noqa: E501

        The Story ID of the object Story.  # noqa: E501

        :return: The object_id of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this HistoryActionStoryLinkUpdate.

        The Story ID of the object Story.  # noqa: E501

        :param object_id: The object_id of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :type: int
        """
        if object_id is None:
            # This should not be here...
            True

        self._object_id = object_id

    @property
    def changes(self):
        """Gets the changes of this HistoryActionStoryLinkUpdate.  # noqa: E501


        :return: The changes of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :rtype: HistoryChangesStoryLink
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this HistoryActionStoryLinkUpdate.


        :param changes: The changes of this HistoryActionStoryLinkUpdate.  # noqa: E501
        :type: HistoryChangesStoryLink
        """
        if changes is None:
            # This should not be here...
            True

        self._changes = changes

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
        if issubclass(HistoryActionStoryLinkUpdate, dict):
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
        if not isinstance(other, HistoryActionStoryLinkUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
