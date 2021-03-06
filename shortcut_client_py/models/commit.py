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

class Commit(object):
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
        'entity_type': 'str',
        'author_id': 'str',
        'hash': 'str',
        'updated_at': 'datetime',
        'merged_branch_ids': 'list[int]',
        'id': 'int',
        'url': 'str',
        'author_email': 'str',
        'timestamp': 'datetime',
        'author_identity': 'Identity',
        'repository_id': 'int',
        'created_at': 'datetime',
        'message': 'str'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'author_id': 'author_id',
        'hash': 'hash',
        'updated_at': 'updated_at',
        'merged_branch_ids': 'merged_branch_ids',
        'id': 'id',
        'url': 'url',
        'author_email': 'author_email',
        'timestamp': 'timestamp',
        'author_identity': 'author_identity',
        'repository_id': 'repository_id',
        'created_at': 'created_at',
        'message': 'message'
    }

    def __init__(self, entity_type=None, author_id=None, hash=None, updated_at=None, merged_branch_ids=None, id=None, url=None, author_email=None, timestamp=None, author_identity=None, repository_id=None, created_at=None, message=None):  # noqa: E501
        """Commit - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._author_id = None
        self._hash = None
        self._updated_at = None
        self._merged_branch_ids = None
        self._id = None
        self._url = None
        self._author_email = None
        self._timestamp = None
        self._author_identity = None
        self._repository_id = None
        self._created_at = None
        self._message = None
        self.discriminator = None
        self.entity_type = entity_type
        self.author_id = author_id
        self.hash = hash
        self.updated_at = updated_at
        self.merged_branch_ids = merged_branch_ids
        self.id = id
        self.url = url
        self.author_email = author_email
        self.timestamp = timestamp
        self.author_identity = author_identity
        self.repository_id = repository_id
        self.created_at = created_at
        self.message = message

    @property
    def entity_type(self):
        """Gets the entity_type of this Commit.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Commit.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this Commit.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            # This should not be here...
            True

        self._entity_type = entity_type

    @property
    def author_id(self):
        """Gets the author_id of this Commit.  # noqa: E501

        The ID of the Member that authored the Commit, if known.  # noqa: E501

        :return: The author_id of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this Commit.

        The ID of the Member that authored the Commit, if known.  # noqa: E501

        :param author_id: The author_id of this Commit.  # noqa: E501
        :type: str
        """
        if author_id is None:
            # This should not be here...
            True

        self._author_id = author_id

    @property
    def hash(self):
        """Gets the hash of this Commit.  # noqa: E501

        The Commit hash.  # noqa: E501

        :return: The hash of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Commit.

        The Commit hash.  # noqa: E501

        :param hash: The hash of this Commit.  # noqa: E501
        :type: str
        """
        if hash is None:
            # This should not be here...
            True

        self._hash = hash

    @property
    def updated_at(self):
        """Gets the updated_at of this Commit.  # noqa: E501

        The time/date the Commit was updated.  # noqa: E501

        :return: The updated_at of this Commit.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Commit.

        The time/date the Commit was updated.  # noqa: E501

        :param updated_at: The updated_at of this Commit.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            # This should not be here...
            True

        self._updated_at = updated_at

    @property
    def merged_branch_ids(self):
        """Gets the merged_branch_ids of this Commit.  # noqa: E501

        The IDs of the Branches the Commit has been merged into.  # noqa: E501

        :return: The merged_branch_ids of this Commit.  # noqa: E501
        :rtype: list[int]
        """
        return self._merged_branch_ids

    @merged_branch_ids.setter
    def merged_branch_ids(self, merged_branch_ids):
        """Sets the merged_branch_ids of this Commit.

        The IDs of the Branches the Commit has been merged into.  # noqa: E501

        :param merged_branch_ids: The merged_branch_ids of this Commit.  # noqa: E501
        :type: list[int]
        """
        if merged_branch_ids is None:
            # This should not be here...
            True

        self._merged_branch_ids = merged_branch_ids

    @property
    def id(self):
        """Gets the id of this Commit.  # noqa: E501

        The unique ID of the Commit.  # noqa: E501

        :return: The id of this Commit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Commit.

        The unique ID of the Commit.  # noqa: E501

        :param id: The id of this Commit.  # noqa: E501
        :type: int
        """
        if id is None:
            # This should not be here...
            True

        self._id = id

    @property
    def url(self):
        """Gets the url of this Commit.  # noqa: E501

        The URL of the Commit.  # noqa: E501

        :return: The url of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Commit.

        The URL of the Commit.  # noqa: E501

        :param url: The url of this Commit.  # noqa: E501
        :type: str
        """
        if url is None:
            # This should not be here...
            True

        self._url = url

    @property
    def author_email(self):
        """Gets the author_email of this Commit.  # noqa: E501

        The email address of the VCS user that authored the Commit.  # noqa: E501

        :return: The author_email of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """Sets the author_email of this Commit.

        The email address of the VCS user that authored the Commit.  # noqa: E501

        :param author_email: The author_email of this Commit.  # noqa: E501
        :type: str
        """
        if author_email is None:
            # This should not be here...
            True

        self._author_email = author_email

    @property
    def timestamp(self):
        """Gets the timestamp of this Commit.  # noqa: E501

        The time/date the Commit was pushed.  # noqa: E501

        :return: The timestamp of this Commit.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Commit.

        The time/date the Commit was pushed.  # noqa: E501

        :param timestamp: The timestamp of this Commit.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            # This should not be here...
            True

        self._timestamp = timestamp

    @property
    def author_identity(self):
        """Gets the author_identity of this Commit.  # noqa: E501


        :return: The author_identity of this Commit.  # noqa: E501
        :rtype: Identity
        """
        return self._author_identity

    @author_identity.setter
    def author_identity(self, author_identity):
        """Sets the author_identity of this Commit.


        :param author_identity: The author_identity of this Commit.  # noqa: E501
        :type: Identity
        """
        if author_identity is None:
            # This should not be here...
            True

        self._author_identity = author_identity

    @property
    def repository_id(self):
        """Gets the repository_id of this Commit.  # noqa: E501

        The ID of the Repository that contains the Commit.  # noqa: E501

        :return: The repository_id of this Commit.  # noqa: E501
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this Commit.

        The ID of the Repository that contains the Commit.  # noqa: E501

        :param repository_id: The repository_id of this Commit.  # noqa: E501
        :type: int
        """
        if repository_id is None:
            # This should not be here...
            True

        self._repository_id = repository_id

    @property
    def created_at(self):
        """Gets the created_at of this Commit.  # noqa: E501

        The time/date the Commit was created.  # noqa: E501

        :return: The created_at of this Commit.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Commit.

        The time/date the Commit was created.  # noqa: E501

        :param created_at: The created_at of this Commit.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            # This should not be here...
            True

        self._created_at = created_at

    @property
    def message(self):
        """Gets the message of this Commit.  # noqa: E501

        The Commit message.  # noqa: E501

        :return: The message of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Commit.

        The Commit message.  # noqa: E501

        :param message: The message of this Commit.  # noqa: E501
        :type: str
        """
        if message is None:
            # This should not be here...
            True

        self._message = message

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
        if issubclass(Commit, dict):
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
        if not isinstance(other, Commit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
