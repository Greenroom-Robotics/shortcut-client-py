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

class CreateEpic(object):
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
        'labels': 'list[CreateLabelParams]',
        'completed_at_override': 'datetime',
        'name': 'str',
        'planned_start_date': 'datetime',
        'state': 'str',
        'milestone_id': 'int',
        'requested_by_id': 'str',
        'epic_state_id': 'int',
        'started_at_override': 'datetime',
        'group_id': 'str',
        'updated_at': 'datetime',
        'follower_ids': 'list[str]',
        'owner_ids': 'list[str]',
        'external_id': 'str',
        'deadline': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'labels': 'labels',
        'completed_at_override': 'completed_at_override',
        'name': 'name',
        'planned_start_date': 'planned_start_date',
        'state': 'state',
        'milestone_id': 'milestone_id',
        'requested_by_id': 'requested_by_id',
        'epic_state_id': 'epic_state_id',
        'started_at_override': 'started_at_override',
        'group_id': 'group_id',
        'updated_at': 'updated_at',
        'follower_ids': 'follower_ids',
        'owner_ids': 'owner_ids',
        'external_id': 'external_id',
        'deadline': 'deadline',
        'created_at': 'created_at'
    }

    def __init__(self, description=None, labels=None, completed_at_override=None, name=None, planned_start_date=None, state=None, milestone_id=None, requested_by_id=None, epic_state_id=None, started_at_override=None, group_id=None, updated_at=None, follower_ids=None, owner_ids=None, external_id=None, deadline=None, created_at=None):  # noqa: E501
        """CreateEpic - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._labels = None
        self._completed_at_override = None
        self._name = None
        self._planned_start_date = None
        self._state = None
        self._milestone_id = None
        self._requested_by_id = None
        self._epic_state_id = None
        self._started_at_override = None
        self._group_id = None
        self._updated_at = None
        self._follower_ids = None
        self._owner_ids = None
        self._external_id = None
        self._deadline = None
        self._created_at = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if completed_at_override is not None:
            self.completed_at_override = completed_at_override
        self.name = name
        if planned_start_date is not None:
            self.planned_start_date = planned_start_date
        if state is not None:
            self.state = state
        if milestone_id is not None:
            self.milestone_id = milestone_id
        if requested_by_id is not None:
            self.requested_by_id = requested_by_id
        if epic_state_id is not None:
            self.epic_state_id = epic_state_id
        if started_at_override is not None:
            self.started_at_override = started_at_override
        if group_id is not None:
            self.group_id = group_id
        if updated_at is not None:
            self.updated_at = updated_at
        if follower_ids is not None:
            self.follower_ids = follower_ids
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if external_id is not None:
            self.external_id = external_id
        if deadline is not None:
            self.deadline = deadline
        if created_at is not None:
            self.created_at = created_at

    @property
    def description(self):
        """Gets the description of this CreateEpic.  # noqa: E501

        The Epic's description.  # noqa: E501

        :return: The description of this CreateEpic.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEpic.

        The Epic's description.  # noqa: E501

        :param description: The description of this CreateEpic.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this CreateEpic.  # noqa: E501

        An array of Labels attached to the Epic.  # noqa: E501

        :return: The labels of this CreateEpic.  # noqa: E501
        :rtype: list[CreateLabelParams]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateEpic.

        An array of Labels attached to the Epic.  # noqa: E501

        :param labels: The labels of this CreateEpic.  # noqa: E501
        :type: list[CreateLabelParams]
        """

        self._labels = labels

    @property
    def completed_at_override(self):
        """Gets the completed_at_override of this CreateEpic.  # noqa: E501

        A manual override for the time/date the Epic was completed.  # noqa: E501

        :return: The completed_at_override of this CreateEpic.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at_override

    @completed_at_override.setter
    def completed_at_override(self, completed_at_override):
        """Sets the completed_at_override of this CreateEpic.

        A manual override for the time/date the Epic was completed.  # noqa: E501

        :param completed_at_override: The completed_at_override of this CreateEpic.  # noqa: E501
        :type: datetime
        """

        self._completed_at_override = completed_at_override

    @property
    def name(self):
        """Gets the name of this CreateEpic.  # noqa: E501

        The Epic's name.  # noqa: E501

        :return: The name of this CreateEpic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEpic.

        The Epic's name.  # noqa: E501

        :param name: The name of this CreateEpic.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def planned_start_date(self):
        """Gets the planned_start_date of this CreateEpic.  # noqa: E501

        The Epic's planned start date.  # noqa: E501

        :return: The planned_start_date of this CreateEpic.  # noqa: E501
        :rtype: datetime
        """
        return self._planned_start_date

    @planned_start_date.setter
    def planned_start_date(self, planned_start_date):
        """Sets the planned_start_date of this CreateEpic.

        The Epic's planned start date.  # noqa: E501

        :param planned_start_date: The planned_start_date of this CreateEpic.  # noqa: E501
        :type: datetime
        """

        self._planned_start_date = planned_start_date

    @property
    def state(self):
        """Gets the state of this CreateEpic.  # noqa: E501

        `Deprecated` The Epic's state (to do, in progress, or done); will be ignored when `epic_state_id` is set.  # noqa: E501

        :return: The state of this CreateEpic.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateEpic.

        `Deprecated` The Epic's state (to do, in progress, or done); will be ignored when `epic_state_id` is set.  # noqa: E501

        :param state: The state of this CreateEpic.  # noqa: E501
        :type: str
        """
        allowed_values = ["in progress", "to do", "done"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def milestone_id(self):
        """Gets the milestone_id of this CreateEpic.  # noqa: E501

        The ID of the Milestone this Epic is related to.  # noqa: E501

        :return: The milestone_id of this CreateEpic.  # noqa: E501
        :rtype: int
        """
        return self._milestone_id

    @milestone_id.setter
    def milestone_id(self, milestone_id):
        """Sets the milestone_id of this CreateEpic.

        The ID of the Milestone this Epic is related to.  # noqa: E501

        :param milestone_id: The milestone_id of this CreateEpic.  # noqa: E501
        :type: int
        """

        self._milestone_id = milestone_id

    @property
    def requested_by_id(self):
        """Gets the requested_by_id of this CreateEpic.  # noqa: E501

        The ID of the member that requested the epic.  # noqa: E501

        :return: The requested_by_id of this CreateEpic.  # noqa: E501
        :rtype: str
        """
        return self._requested_by_id

    @requested_by_id.setter
    def requested_by_id(self, requested_by_id):
        """Sets the requested_by_id of this CreateEpic.

        The ID of the member that requested the epic.  # noqa: E501

        :param requested_by_id: The requested_by_id of this CreateEpic.  # noqa: E501
        :type: str
        """

        self._requested_by_id = requested_by_id

    @property
    def epic_state_id(self):
        """Gets the epic_state_id of this CreateEpic.  # noqa: E501

        The ID of the Epic State.  # noqa: E501

        :return: The epic_state_id of this CreateEpic.  # noqa: E501
        :rtype: int
        """
        return self._epic_state_id

    @epic_state_id.setter
    def epic_state_id(self, epic_state_id):
        """Sets the epic_state_id of this CreateEpic.

        The ID of the Epic State.  # noqa: E501

        :param epic_state_id: The epic_state_id of this CreateEpic.  # noqa: E501
        :type: int
        """

        self._epic_state_id = epic_state_id

    @property
    def started_at_override(self):
        """Gets the started_at_override of this CreateEpic.  # noqa: E501

        A manual override for the time/date the Epic was started.  # noqa: E501

        :return: The started_at_override of this CreateEpic.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at_override

    @started_at_override.setter
    def started_at_override(self, started_at_override):
        """Sets the started_at_override of this CreateEpic.

        A manual override for the time/date the Epic was started.  # noqa: E501

        :param started_at_override: The started_at_override of this CreateEpic.  # noqa: E501
        :type: datetime
        """

        self._started_at_override = started_at_override

    @property
    def group_id(self):
        """Gets the group_id of this CreateEpic.  # noqa: E501

        The ID of the group to associate with the epic.  # noqa: E501

        :return: The group_id of this CreateEpic.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateEpic.

        The ID of the group to associate with the epic.  # noqa: E501

        :param group_id: The group_id of this CreateEpic.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateEpic.  # noqa: E501

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :return: The updated_at of this CreateEpic.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateEpic.

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :param updated_at: The updated_at of this CreateEpic.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def follower_ids(self):
        """Gets the follower_ids of this CreateEpic.  # noqa: E501

        An array of UUIDs for any Members you want to add as Followers on this new Epic.  # noqa: E501

        :return: The follower_ids of this CreateEpic.  # noqa: E501
        :rtype: list[str]
        """
        return self._follower_ids

    @follower_ids.setter
    def follower_ids(self, follower_ids):
        """Sets the follower_ids of this CreateEpic.

        An array of UUIDs for any Members you want to add as Followers on this new Epic.  # noqa: E501

        :param follower_ids: The follower_ids of this CreateEpic.  # noqa: E501
        :type: list[str]
        """

        self._follower_ids = follower_ids

    @property
    def owner_ids(self):
        """Gets the owner_ids of this CreateEpic.  # noqa: E501

        An array of UUIDs for any members you want to add as Owners on this new Epic.  # noqa: E501

        :return: The owner_ids of this CreateEpic.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this CreateEpic.

        An array of UUIDs for any members you want to add as Owners on this new Epic.  # noqa: E501

        :param owner_ids: The owner_ids of this CreateEpic.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids = owner_ids

    @property
    def external_id(self):
        """Gets the external_id of this CreateEpic.  # noqa: E501

        This field can be set to another unique ID. In the case that the Epic has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this CreateEpic.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateEpic.

        This field can be set to another unique ID. In the case that the Epic has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this CreateEpic.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def deadline(self):
        """Gets the deadline of this CreateEpic.  # noqa: E501

        The Epic's deadline.  # noqa: E501

        :return: The deadline of this CreateEpic.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this CreateEpic.

        The Epic's deadline.  # noqa: E501

        :param deadline: The deadline of this CreateEpic.  # noqa: E501
        :type: datetime
        """

        self._deadline = deadline

    @property
    def created_at(self):
        """Gets the created_at of this CreateEpic.  # noqa: E501

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :return: The created_at of this CreateEpic.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateEpic.

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :param created_at: The created_at of this CreateEpic.  # noqa: E501
        :type: datetime
        """

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
        if issubclass(CreateEpic, dict):
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
        if not isinstance(other, CreateEpic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
