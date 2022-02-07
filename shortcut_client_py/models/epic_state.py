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

class EpicState(object):
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
        'entity_type': 'str',
        'color': 'str',
        'name': 'str',
        'global_id': 'str',
        'type': 'str',
        'updated_at': 'datetime',
        'id': 'int',
        'position': 'int',
        'created_at': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'entity_type': 'entity_type',
        'color': 'color',
        'name': 'name',
        'global_id': 'global_id',
        'type': 'type',
        'updated_at': 'updated_at',
        'id': 'id',
        'position': 'position',
        'created_at': 'created_at'
    }

    def __init__(self, description=None, entity_type=None, color=None, name=None, global_id=None, type=None, updated_at=None, id=None, position=None, created_at=None):  # noqa: E501
        """EpicState - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._entity_type = None
        self._color = None
        self._name = None
        self._global_id = None
        self._type = None
        self._updated_at = None
        self._id = None
        self._position = None
        self._created_at = None
        self.discriminator = None
        self.description = description
        self.entity_type = entity_type
        if color is not None:
            self.color = color
        self.name = name
        self.global_id = global_id
        self.type = type
        self.updated_at = updated_at
        self.id = id
        self.position = position
        self.created_at = created_at

    @property
    def description(self):
        """Gets the description of this EpicState.  # noqa: E501

        The description of what sort of Epics belong in that Epic State.  # noqa: E501

        :return: The description of this EpicState.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EpicState.

        The description of what sort of Epics belong in that Epic State.  # noqa: E501

        :param description: The description of this EpicState.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def entity_type(self):
        """Gets the entity_type of this EpicState.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this EpicState.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EpicState.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this EpicState.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def color(self):
        """Gets the color of this EpicState.  # noqa: E501

        The hex color for this Epic State.  # noqa: E501

        :return: The color of this EpicState.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this EpicState.

        The hex color for this Epic State.  # noqa: E501

        :param color: The color of this EpicState.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def name(self):
        """Gets the name of this EpicState.  # noqa: E501

        The Epic State's name.  # noqa: E501

        :return: The name of this EpicState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EpicState.

        The Epic State's name.  # noqa: E501

        :param name: The name of this EpicState.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def global_id(self):
        """Gets the global_id of this EpicState.  # noqa: E501


        :return: The global_id of this EpicState.  # noqa: E501
        :rtype: str
        """
        return self._global_id

    @global_id.setter
    def global_id(self, global_id):
        """Sets the global_id of this EpicState.


        :param global_id: The global_id of this EpicState.  # noqa: E501
        :type: str
        """
        if global_id is None:
            raise ValueError("Invalid value for `global_id`, must not be `None`")  # noqa: E501

        self._global_id = global_id

    @property
    def type(self):
        """Gets the type of this EpicState.  # noqa: E501

        The type of Epic State (Unstarted, Started, or Done)  # noqa: E501

        :return: The type of this EpicState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EpicState.

        The type of Epic State (Unstarted, Started, or Done)  # noqa: E501

        :param type: The type of this EpicState.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this EpicState.  # noqa: E501

        When the Epic State was last updated.  # noqa: E501

        :return: The updated_at of this EpicState.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EpicState.

        When the Epic State was last updated.  # noqa: E501

        :param updated_at: The updated_at of this EpicState.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this EpicState.  # noqa: E501

        The unique ID of the Epic State.  # noqa: E501

        :return: The id of this EpicState.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EpicState.

        The unique ID of the Epic State.  # noqa: E501

        :param id: The id of this EpicState.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def position(self):
        """Gets the position of this EpicState.  # noqa: E501

        The position that the Epic State is in, starting with 0 at the left.  # noqa: E501

        :return: The position of this EpicState.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this EpicState.

        The position that the Epic State is in, starting with 0 at the left.  # noqa: E501

        :param position: The position of this EpicState.  # noqa: E501
        :type: int
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def created_at(self):
        """Gets the created_at of this EpicState.  # noqa: E501

        The time/date the Epic State was created.  # noqa: E501

        :return: The created_at of this EpicState.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EpicState.

        The time/date the Epic State was created.  # noqa: E501

        :param created_at: The created_at of this EpicState.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(EpicState, dict):
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
        if not isinstance(other, EpicState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other