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

class StoryComment(object):
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
        'entity_type': 'str',
        'deleted': 'bool',
        'story_id': 'int',
        'mention_ids': 'list[str]',
        'author_id': 'str',
        'member_mention_ids': 'list[str]',
        'updated_at': 'datetime',
        'group_mention_ids': 'list[str]',
        'external_id': 'str',
        'parent_id': 'int',
        'id': 'int',
        'position': 'int',
        'reactions': 'list[StoryReaction]',
        'created_at': 'datetime',
        'text': 'str'
    }

    attribute_map = {
        'app_url': 'app_url',
        'entity_type': 'entity_type',
        'deleted': 'deleted',
        'story_id': 'story_id',
        'mention_ids': 'mention_ids',
        'author_id': 'author_id',
        'member_mention_ids': 'member_mention_ids',
        'updated_at': 'updated_at',
        'group_mention_ids': 'group_mention_ids',
        'external_id': 'external_id',
        'parent_id': 'parent_id',
        'id': 'id',
        'position': 'position',
        'reactions': 'reactions',
        'created_at': 'created_at',
        'text': 'text'
    }

    def __init__(self, app_url=None, entity_type=None, deleted=None, story_id=None, mention_ids=None, author_id=None, member_mention_ids=None, updated_at=None, group_mention_ids=None, external_id=None, parent_id=None, id=None, position=None, reactions=None, created_at=None, text=None):  # noqa: E501
        """StoryComment - a model defined in Swagger"""  # noqa: E501
        self._app_url = None
        self._entity_type = None
        self._deleted = None
        self._story_id = None
        self._mention_ids = None
        self._author_id = None
        self._member_mention_ids = None
        self._updated_at = None
        self._group_mention_ids = None
        self._external_id = None
        self._parent_id = None
        self._id = None
        self._position = None
        self._reactions = None
        self._created_at = None
        self._text = None
        self.discriminator = None
        self.app_url = app_url
        self.entity_type = entity_type
        self.deleted = deleted
        self.story_id = story_id
        self.mention_ids = mention_ids
        self.author_id = author_id
        self.member_mention_ids = member_mention_ids
        self.updated_at = updated_at
        self.group_mention_ids = group_mention_ids
        self.external_id = external_id
        if parent_id is not None:
            self.parent_id = parent_id
        self.id = id
        self.position = position
        self.reactions = reactions
        self.created_at = created_at
        self.text = text

    @property
    def app_url(self):
        """Gets the app_url of this StoryComment.  # noqa: E501

        The Shortcut application url for the Comment.  # noqa: E501

        :return: The app_url of this StoryComment.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this StoryComment.

        The Shortcut application url for the Comment.  # noqa: E501

        :param app_url: The app_url of this StoryComment.  # noqa: E501
        :type: str
        """
        if app_url is None:
            # This should not be here...
            True

        self._app_url = app_url

    @property
    def entity_type(self):
        """Gets the entity_type of this StoryComment.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this StoryComment.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this StoryComment.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this StoryComment.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def deleted(self):
        """Gets the deleted of this StoryComment.  # noqa: E501

        True/false boolean indicating whether the Comment has been deleted.  # noqa: E501

        :return: The deleted of this StoryComment.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this StoryComment.

        True/false boolean indicating whether the Comment has been deleted.  # noqa: E501

        :param deleted: The deleted of this StoryComment.  # noqa: E501
        :type: bool
        """
        if deleted is None:
            # This should not be here...
            True

        self._deleted = deleted

    @property
    def story_id(self):
        """Gets the story_id of this StoryComment.  # noqa: E501

        The ID of the Story on which the Comment appears.  # noqa: E501

        :return: The story_id of this StoryComment.  # noqa: E501
        :rtype: int
        """
        return self._story_id

    @story_id.setter
    def story_id(self, story_id):
        """Sets the story_id of this StoryComment.

        The ID of the Story on which the Comment appears.  # noqa: E501

        :param story_id: The story_id of this StoryComment.  # noqa: E501
        :type: int
        """
        if story_id is None:
            # This should not be here...
            True

        self._story_id = story_id

    @property
    def mention_ids(self):
        """Gets the mention_ids of this StoryComment.  # noqa: E501

        Deprecated: use member_mention_ids.  # noqa: E501

        :return: The mention_ids of this StoryComment.  # noqa: E501
        :rtype: list[str]
        """
        return self._mention_ids

    @mention_ids.setter
    def mention_ids(self, mention_ids):
        """Sets the mention_ids of this StoryComment.

        Deprecated: use member_mention_ids.  # noqa: E501

        :param mention_ids: The mention_ids of this StoryComment.  # noqa: E501
        :type: list[str]
        """
        if mention_ids is None:
            # This should not be here...
            True

        self._mention_ids = mention_ids

    @property
    def author_id(self):
        """Gets the author_id of this StoryComment.  # noqa: E501

        The unique ID of the Member who is the Comment's author.  # noqa: E501

        :return: The author_id of this StoryComment.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this StoryComment.

        The unique ID of the Member who is the Comment's author.  # noqa: E501

        :param author_id: The author_id of this StoryComment.  # noqa: E501
        :type: str
        """
        if author_id is None:
            # This should not be here...
            True

        self._author_id = author_id

    @property
    def member_mention_ids(self):
        """Gets the member_mention_ids of this StoryComment.  # noqa: E501

        The unique IDs of the Member who are mentioned in the Comment.  # noqa: E501

        :return: The member_mention_ids of this StoryComment.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_mention_ids

    @member_mention_ids.setter
    def member_mention_ids(self, member_mention_ids):
        """Sets the member_mention_ids of this StoryComment.

        The unique IDs of the Member who are mentioned in the Comment.  # noqa: E501

        :param member_mention_ids: The member_mention_ids of this StoryComment.  # noqa: E501
        :type: list[str]
        """
        if member_mention_ids is None:
            # This should not be here...
            True

        self._member_mention_ids = member_mention_ids

    @property
    def updated_at(self):
        """Gets the updated_at of this StoryComment.  # noqa: E501

        The time/date when the Comment was updated.  # noqa: E501

        :return: The updated_at of this StoryComment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this StoryComment.

        The time/date when the Comment was updated.  # noqa: E501

        :param updated_at: The updated_at of this StoryComment.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            # This should not be here...
            True

        self._updated_at = updated_at

    @property
    def group_mention_ids(self):
        """Gets the group_mention_ids of this StoryComment.  # noqa: E501

        The unique IDs of the Group who are mentioned in the Comment.  # noqa: E501

        :return: The group_mention_ids of this StoryComment.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_mention_ids

    @group_mention_ids.setter
    def group_mention_ids(self, group_mention_ids):
        """Sets the group_mention_ids of this StoryComment.

        The unique IDs of the Group who are mentioned in the Comment.  # noqa: E501

        :param group_mention_ids: The group_mention_ids of this StoryComment.  # noqa: E501
        :type: list[str]
        """
        if group_mention_ids is None:
            # This should not be here...
            True

        self._group_mention_ids = group_mention_ids

    @property
    def external_id(self):
        """Gets the external_id of this StoryComment.  # noqa: E501

        This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this StoryComment.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this StoryComment.

        This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this StoryComment.  # noqa: E501
        :type: str
        """
        if external_id is None:
            # This should not be here...
            True

        self._external_id = external_id

    @property
    def parent_id(self):
        """Gets the parent_id of this StoryComment.  # noqa: E501

        The ID of the parent Comment this Comment is threaded under.  # noqa: E501

        :return: The parent_id of this StoryComment.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this StoryComment.

        The ID of the parent Comment this Comment is threaded under.  # noqa: E501

        :param parent_id: The parent_id of this StoryComment.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def id(self):
        """Gets the id of this StoryComment.  # noqa: E501

        The unique ID of the Comment.  # noqa: E501

        :return: The id of this StoryComment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoryComment.

        The unique ID of the Comment.  # noqa: E501

        :param id: The id of this StoryComment.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def position(self):
        """Gets the position of this StoryComment.  # noqa: E501

        The Comments numerical position in the list from oldest to newest.  # noqa: E501

        :return: The position of this StoryComment.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this StoryComment.

        The Comments numerical position in the list from oldest to newest.  # noqa: E501

        :param position: The position of this StoryComment.  # noqa: E501
        :type: int
        """
        if position is None:
            # This should not be here...
            True

        self._position = position

    @property
    def reactions(self):
        """Gets the reactions of this StoryComment.  # noqa: E501

        A set of Reactions to this Comment.  # noqa: E501

        :return: The reactions of this StoryComment.  # noqa: E501
        :rtype: list[StoryReaction]
        """
        return self._reactions

    @reactions.setter
    def reactions(self, reactions):
        """Sets the reactions of this StoryComment.

        A set of Reactions to this Comment.  # noqa: E501

        :param reactions: The reactions of this StoryComment.  # noqa: E501
        :type: list[StoryReaction]
        """
        if reactions is None:
            # This should not be here...
            True

        self._reactions = reactions

    @property
    def created_at(self):
        """Gets the created_at of this StoryComment.  # noqa: E501

        The time/date when the Comment was created.  # noqa: E501

        :return: The created_at of this StoryComment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StoryComment.

        The time/date when the Comment was created.  # noqa: E501

        :param created_at: The created_at of this StoryComment.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            # This should not be here...
            True

        self._created_at = created_at

    @property
    def text(self):
        """Gets the text of this StoryComment.  # noqa: E501

        The text of the Comment. In the case that the Comment has been deleted, this field can be set to nil.  # noqa: E501

        :return: The text of this StoryComment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this StoryComment.

        The text of the Comment. In the case that the Comment has been deleted, this field can be set to nil.  # noqa: E501

        :param text: The text of this StoryComment.  # noqa: E501
        :type: str
        """
        if text is None:
            # This should not be here...
            True

        self._text = text

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
        if issubclass(StoryComment, dict):
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
        if not isinstance(other, StoryComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
