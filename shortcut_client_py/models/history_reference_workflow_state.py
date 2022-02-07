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

class HistoryReferenceWorkflowState(object):
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
        'type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entity_type',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, id=None, entity_type=None, type=None, name=None):  # noqa: E501
        """HistoryReferenceWorkflowState - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity_type = None
        self._type = None
        self._name = None
        self.discriminator = None
        self.id = id
        self.entity_type = entity_type
        self.type = type
        self.name = name

    @property
    def id(self):
        """Gets the id of this HistoryReferenceWorkflowState.  # noqa: E501

        The ID of the entity referenced.  # noqa: E501

        :return: The id of this HistoryReferenceWorkflowState.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryReferenceWorkflowState.

        The ID of the entity referenced.  # noqa: E501

        :param id: The id of this HistoryReferenceWorkflowState.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this HistoryReferenceWorkflowState.  # noqa: E501

        The type of entity referenced.  # noqa: E501

        :return: The entity_type of this HistoryReferenceWorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this HistoryReferenceWorkflowState.

        The type of entity referenced.  # noqa: E501

        :param entity_type: The entity_type of this HistoryReferenceWorkflowState.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def type(self):
        """Gets the type of this HistoryReferenceWorkflowState.  # noqa: E501

        Either \"unstarted\", \"started\", or \"done\".  # noqa: E501

        :return: The type of this HistoryReferenceWorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HistoryReferenceWorkflowState.

        Either \"unstarted\", \"started\", or \"done\".  # noqa: E501

        :param type: The type of this HistoryReferenceWorkflowState.  # noqa: E501
        :type: str
        """
        if type is None:
            # This should not be here...
            True
        allowed_values = ["started", "unstarted", "done"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this HistoryReferenceWorkflowState.  # noqa: E501

        The name of the entity referenced.  # noqa: E501

        :return: The name of this HistoryReferenceWorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HistoryReferenceWorkflowState.

        The name of the entity referenced.  # noqa: E501

        :param name: The name of this HistoryReferenceWorkflowState.  # noqa: E501
        :type: str
        """
        if name is None:
            # This should not be here...
            True

        self._name = name

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
        if issubclass(HistoryReferenceWorkflowState, dict):
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
        if not isinstance(other, HistoryReferenceWorkflowState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
