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

class LabelSlim(object):
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
        'app_url': 'str',
        'description': 'str',
        'archived': 'bool',
        'entity_type': 'str',
        'color': 'str',
        'name': 'str',
        'global_id': 'str',
        'updated_at': 'datetime',
        'external_id': 'str',
        'id': 'int',
        'created_at': 'datetime'
    }

    attribute_map = {
        'app_url': 'app_url',
        'description': 'description',
        'archived': 'archived',
        'entity_type': 'entity_type',
        'color': 'color',
        'name': 'name',
        'global_id': 'global_id',
        'updated_at': 'updated_at',
        'external_id': 'external_id',
        'id': 'id',
        'created_at': 'created_at'
    }

    def __init__(self, app_url=None, description=None, archived=None, entity_type=None, color=None, name=None, global_id=None, updated_at=None, external_id=None, id=None, created_at=None):  # noqa: E501
        """LabelSlim - a model defined in Swagger"""  # noqa: E501
        self._app_url = None
        self._description = None
        self._archived = None
        self._entity_type = None
        self._color = None
        self._name = None
        self._global_id = None
        self._updated_at = None
        self._external_id = None
        self._id = None
        self._created_at = None
        self.discriminator = None
        self.app_url = app_url
        self.description = description
        self.archived = archived
        self.entity_type = entity_type
        self.color = color
        self.name = name
        self.global_id = global_id
        self.updated_at = updated_at
        self.external_id = external_id
        self.id = id
        self.created_at = created_at

    @property
    def app_url(self):
        """Gets the app_url of this LabelSlim.  # noqa: E501

        The Shortcut application url for the Label.  # noqa: E501

        :return: The app_url of this LabelSlim.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this LabelSlim.

        The Shortcut application url for the Label.  # noqa: E501

        :param app_url: The app_url of this LabelSlim.  # noqa: E501
        :type: str
        """
        if app_url is None:
            # This should not be here...
            True

        self._app_url = app_url

    @property
    def description(self):
        """Gets the description of this LabelSlim.  # noqa: E501

        The description of the Label.  # noqa: E501

        :return: The description of this LabelSlim.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LabelSlim.

        The description of the Label.  # noqa: E501

        :param description: The description of this LabelSlim.  # noqa: E501
        :type: str
        """
        if description is None:
            # This should not be here...
            True

        self._description = description

    @property
    def archived(self):
        """Gets the archived of this LabelSlim.  # noqa: E501

        A true/false boolean indicating if the Label has been archived.  # noqa: E501

        :return: The archived of this LabelSlim.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this LabelSlim.

        A true/false boolean indicating if the Label has been archived.  # noqa: E501

        :param archived: The archived of this LabelSlim.  # noqa: E501
        :type: bool
        """
        if archived is None:
            # This should not be here...
            True

        self._archived = archived

    @property
    def entity_type(self):
        """Gets the entity_type of this LabelSlim.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this LabelSlim.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this LabelSlim.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this LabelSlim.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def color(self):
        """Gets the color of this LabelSlim.  # noqa: E501

        The hex color to be displayed with the Label (for example, \"#ff0000\").  # noqa: E501

        :return: The color of this LabelSlim.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this LabelSlim.

        The hex color to be displayed with the Label (for example, \"#ff0000\").  # noqa: E501

        :param color: The color of this LabelSlim.  # noqa: E501
        :type: str
        """
        if color is None:
            # This should not be here...
            True

        self._color = color

    @property
    def name(self):
        """Gets the name of this LabelSlim.  # noqa: E501

        The name of the Label.  # noqa: E501

        :return: The name of this LabelSlim.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelSlim.

        The name of the Label.  # noqa: E501

        :param name: The name of this LabelSlim.  # noqa: E501
        :type: str
        """
        if name is None:
            # This should not be here...
            True

        self._name = name

    @property
    def global_id(self):
        """Gets the global_id of this LabelSlim.  # noqa: E501


        :return: The global_id of this LabelSlim.  # noqa: E501
        :rtype: str
        """
        return self._global_id

    @global_id.setter
    def global_id(self, global_id):
        """Sets the global_id of this LabelSlim.


        :param global_id: The global_id of this LabelSlim.  # noqa: E501
        :type: str
        """
        if global_id is None:
            # This should not be here...
            True

        self._global_id = global_id

    @property
    def updated_at(self):
        """Gets the updated_at of this LabelSlim.  # noqa: E501

        The time/date that the Label was updated.  # noqa: E501

        :return: The updated_at of this LabelSlim.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LabelSlim.

        The time/date that the Label was updated.  # noqa: E501

        :param updated_at: The updated_at of this LabelSlim.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            # This should not be here...
            True

        self._updated_at = updated_at

    @property
    def external_id(self):
        """Gets the external_id of this LabelSlim.  # noqa: E501

        This field can be set to another unique ID. In the case that the Label has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this LabelSlim.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this LabelSlim.

        This field can be set to another unique ID. In the case that the Label has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this LabelSlim.  # noqa: E501
        :type: str
        """
        if external_id is None:
            # This should not be here...
            True

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this LabelSlim.  # noqa: E501

        The unique ID of the Label.  # noqa: E501

        :return: The id of this LabelSlim.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LabelSlim.

        The unique ID of the Label.  # noqa: E501

        :param id: The id of this LabelSlim.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this LabelSlim.  # noqa: E501

        The time/date that the Label was created.  # noqa: E501

        :return: The created_at of this LabelSlim.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LabelSlim.

        The time/date that the Label was created.  # noqa: E501

        :param created_at: The created_at of this LabelSlim.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            # This should not be here...
            True

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
        if issubclass(LabelSlim, dict):
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
        if not isinstance(other, LabelSlim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
