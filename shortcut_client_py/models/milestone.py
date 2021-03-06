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

class Milestone(object):
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
        'started': 'bool',
        'entity_type': 'str',
        'completed_at_override': 'datetime',
        'started_at': 'datetime',
        'completed_at': 'datetime',
        'name': 'str',
        'global_id': 'str',
        'completed': 'bool',
        'state': 'str',
        'started_at_override': 'datetime',
        'updated_at': 'datetime',
        'categories': 'list[Category]',
        'id': 'int',
        'position': 'int',
        'stats': 'MilestoneStats',
        'created_at': 'datetime'
    }

    attribute_map = {
        'app_url': 'app_url',
        'description': 'description',
        'started': 'started',
        'entity_type': 'entity_type',
        'completed_at_override': 'completed_at_override',
        'started_at': 'started_at',
        'completed_at': 'completed_at',
        'name': 'name',
        'global_id': 'global_id',
        'completed': 'completed',
        'state': 'state',
        'started_at_override': 'started_at_override',
        'updated_at': 'updated_at',
        'categories': 'categories',
        'id': 'id',
        'position': 'position',
        'stats': 'stats',
        'created_at': 'created_at'
    }

    def __init__(self, app_url=None, description=None, started=None, entity_type=None, completed_at_override=None, started_at=None, completed_at=None, name=None, global_id=None, completed=None, state=None, started_at_override=None, updated_at=None, categories=None, id=None, position=None, stats=None, created_at=None):  # noqa: E501
        """Milestone - a model defined in Swagger"""  # noqa: E501
        self._app_url = None
        self._description = None
        self._started = None
        self._entity_type = None
        self._completed_at_override = None
        self._started_at = None
        self._completed_at = None
        self._name = None
        self._global_id = None
        self._completed = None
        self._state = None
        self._started_at_override = None
        self._updated_at = None
        self._categories = None
        self._id = None
        self._position = None
        self._stats = None
        self._created_at = None
        self.discriminator = None
        self.app_url = app_url
        self.description = description
        self.started = started
        self.entity_type = entity_type
        self.completed_at_override = completed_at_override
        self.started_at = started_at
        self.completed_at = completed_at
        self.name = name
        self.global_id = global_id
        self.completed = completed
        self.state = state
        self.started_at_override = started_at_override
        self.updated_at = updated_at
        self.categories = categories
        self.id = id
        self.position = position
        if stats is not None:
            self.stats = stats
        self.created_at = created_at

    @property
    def app_url(self):
        """Gets the app_url of this Milestone.  # noqa: E501

        The Shortcut application url for the Milestone.  # noqa: E501

        :return: The app_url of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this Milestone.

        The Shortcut application url for the Milestone.  # noqa: E501

        :param app_url: The app_url of this Milestone.  # noqa: E501
        :type: str
        """
        if app_url is None:
            # This should not be here...
            True

        self._app_url = app_url

    @property
    def description(self):
        """Gets the description of this Milestone.  # noqa: E501

        The Milestone's description.  # noqa: E501

        :return: The description of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Milestone.

        The Milestone's description.  # noqa: E501

        :param description: The description of this Milestone.  # noqa: E501
        :type: str
        """
        if description is None:
            # This should not be here...
            True

        self._description = description

    @property
    def started(self):
        """Gets the started of this Milestone.  # noqa: E501

        A true/false boolean indicating if the Milestone has been started.  # noqa: E501

        :return: The started of this Milestone.  # noqa: E501
        :rtype: bool
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this Milestone.

        A true/false boolean indicating if the Milestone has been started.  # noqa: E501

        :param started: The started of this Milestone.  # noqa: E501
        :type: bool
        """
        if started is None:
            # This should not be here...
            True

        self._started = started

    @property
    def entity_type(self):
        """Gets the entity_type of this Milestone.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Milestone.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this Milestone.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def completed_at_override(self):
        """Gets the completed_at_override of this Milestone.  # noqa: E501

        A manual override for the time/date the Milestone was completed.  # noqa: E501

        :return: The completed_at_override of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at_override

    @completed_at_override.setter
    def completed_at_override(self, completed_at_override):
        """Sets the completed_at_override of this Milestone.

        A manual override for the time/date the Milestone was completed.  # noqa: E501

        :param completed_at_override: The completed_at_override of this Milestone.  # noqa: E501
        :type: datetime
        """
        if completed_at_override is None:
            # This should not be here...
            True

        self._completed_at_override = completed_at_override

    @property
    def started_at(self):
        """Gets the started_at of this Milestone.  # noqa: E501

        The time/date the Milestone was started.  # noqa: E501

        :return: The started_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Milestone.

        The time/date the Milestone was started.  # noqa: E501

        :param started_at: The started_at of this Milestone.  # noqa: E501
        :type: datetime
        """
        if started_at is None:
            # This should not be here...
            True

        self._started_at = started_at

    @property
    def completed_at(self):
        """Gets the completed_at of this Milestone.  # noqa: E501

        The time/date the Milestone was completed.  # noqa: E501

        :return: The completed_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this Milestone.

        The time/date the Milestone was completed.  # noqa: E501

        :param completed_at: The completed_at of this Milestone.  # noqa: E501
        :type: datetime
        """
        if completed_at is None:
            # This should not be here...
            True

        self._completed_at = completed_at

    @property
    def name(self):
        """Gets the name of this Milestone.  # noqa: E501

        The name of the Milestone.  # noqa: E501

        :return: The name of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Milestone.

        The name of the Milestone.  # noqa: E501

        :param name: The name of this Milestone.  # noqa: E501
        :type: str
        """
        if name is None:
            # This should not be here...
            True

        self._name = name

    @property
    def global_id(self):
        """Gets the global_id of this Milestone.  # noqa: E501


        :return: The global_id of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._global_id

    @global_id.setter
    def global_id(self, global_id):
        """Sets the global_id of this Milestone.


        :param global_id: The global_id of this Milestone.  # noqa: E501
        :type: str
        """
        if global_id is None:
            # This should not be here...
            True

        self._global_id = global_id

    @property
    def completed(self):
        """Gets the completed of this Milestone.  # noqa: E501

        A true/false boolean indicating if the Milestone has been completed.  # noqa: E501

        :return: The completed of this Milestone.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this Milestone.

        A true/false boolean indicating if the Milestone has been completed.  # noqa: E501

        :param completed: The completed of this Milestone.  # noqa: E501
        :type: bool
        """
        if completed is None:
            # This should not be here...
            True

        self._completed = completed

    @property
    def state(self):
        """Gets the state of this Milestone.  # noqa: E501

        The workflow state that the Milestone is in.  # noqa: E501

        :return: The state of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Milestone.

        The workflow state that the Milestone is in.  # noqa: E501

        :param state: The state of this Milestone.  # noqa: E501
        :type: str
        """
        if state is None:
            # This should not be here...
            True

        self._state = state

    @property
    def started_at_override(self):
        """Gets the started_at_override of this Milestone.  # noqa: E501

        A manual override for the time/date the Milestone was started.  # noqa: E501

        :return: The started_at_override of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at_override

    @started_at_override.setter
    def started_at_override(self, started_at_override):
        """Sets the started_at_override of this Milestone.

        A manual override for the time/date the Milestone was started.  # noqa: E501

        :param started_at_override: The started_at_override of this Milestone.  # noqa: E501
        :type: datetime
        """
        if started_at_override is None:
            # This should not be here...
            True

        self._started_at_override = started_at_override

    @property
    def updated_at(self):
        """Gets the updated_at of this Milestone.  # noqa: E501

        The time/date the Milestone was updated.  # noqa: E501

        :return: The updated_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Milestone.

        The time/date the Milestone was updated.  # noqa: E501

        :param updated_at: The updated_at of this Milestone.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            # This should not be here...
            True

        self._updated_at = updated_at

    @property
    def categories(self):
        """Gets the categories of this Milestone.  # noqa: E501

        An array of Categories attached to the Milestone.  # noqa: E501

        :return: The categories of this Milestone.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Milestone.

        An array of Categories attached to the Milestone.  # noqa: E501

        :param categories: The categories of this Milestone.  # noqa: E501
        :type: list[Category]
        """
        if categories is None:
            # This should not be here...
            True

        self._categories = categories

    @property
    def id(self):
        """Gets the id of this Milestone.  # noqa: E501

        The unique ID of the Milestone.  # noqa: E501

        :return: The id of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Milestone.

        The unique ID of the Milestone.  # noqa: E501

        :param id: The id of this Milestone.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def position(self):
        """Gets the position of this Milestone.  # noqa: E501

        A number representing the position of the Milestone in relation to every other Milestone within the Workspace.  # noqa: E501

        :return: The position of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Milestone.

        A number representing the position of the Milestone in relation to every other Milestone within the Workspace.  # noqa: E501

        :param position: The position of this Milestone.  # noqa: E501
        :type: int
        """
        if position is None:
            # This should not be here...
            True

        self._position = position

    @property
    def stats(self):
        """Gets the stats of this Milestone.  # noqa: E501


        :return: The stats of this Milestone.  # noqa: E501
        :rtype: MilestoneStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Milestone.


        :param stats: The stats of this Milestone.  # noqa: E501
        :type: MilestoneStats
        """

        self._stats = stats

    @property
    def created_at(self):
        """Gets the created_at of this Milestone.  # noqa: E501

        The time/date the Milestone was created.  # noqa: E501

        :return: The created_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Milestone.

        The time/date the Milestone was created.  # noqa: E501

        :param created_at: The created_at of this Milestone.  # noqa: E501
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
        if issubclass(Milestone, dict):
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
        if not isinstance(other, Milestone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
