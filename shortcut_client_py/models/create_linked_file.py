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

class CreateLinkedFile(object):
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
        'story_id': 'int',
        'name': 'str',
        'thumbnail_url': 'str',
        'type': 'str',
        'size': 'int',
        'uploader_id': 'str',
        'content_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'description': 'description',
        'story_id': 'story_id',
        'name': 'name',
        'thumbnail_url': 'thumbnail_url',
        'type': 'type',
        'size': 'size',
        'uploader_id': 'uploader_id',
        'content_type': 'content_type',
        'url': 'url'
    }

    def __init__(self, description=None, story_id=None, name=None, thumbnail_url=None, type=None, size=None, uploader_id=None, content_type=None, url=None):  # noqa: E501
        """CreateLinkedFile - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._story_id = None
        self._name = None
        self._thumbnail_url = None
        self._type = None
        self._size = None
        self._uploader_id = None
        self._content_type = None
        self._url = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if story_id is not None:
            self.story_id = story_id
        self.name = name
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        self.type = type
        if size is not None:
            self.size = size
        if uploader_id is not None:
            self.uploader_id = uploader_id
        if content_type is not None:
            self.content_type = content_type
        self.url = url

    @property
    def description(self):
        """Gets the description of this CreateLinkedFile.  # noqa: E501

        The description of the file.  # noqa: E501

        :return: The description of this CreateLinkedFile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLinkedFile.

        The description of the file.  # noqa: E501

        :param description: The description of this CreateLinkedFile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def story_id(self):
        """Gets the story_id of this CreateLinkedFile.  # noqa: E501

        The ID of the linked story.  # noqa: E501

        :return: The story_id of this CreateLinkedFile.  # noqa: E501
        :rtype: int
        """
        return self._story_id

    @story_id.setter
    def story_id(self, story_id):
        """Sets the story_id of this CreateLinkedFile.

        The ID of the linked story.  # noqa: E501

        :param story_id: The story_id of this CreateLinkedFile.  # noqa: E501
        :type: int
        """

        self._story_id = story_id

    @property
    def name(self):
        """Gets the name of this CreateLinkedFile.  # noqa: E501

        The name of the file.  # noqa: E501

        :return: The name of this CreateLinkedFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLinkedFile.

        The name of the file.  # noqa: E501

        :param name: The name of this CreateLinkedFile.  # noqa: E501
        :type: str
        """
        if name is None:
            # This should not be here...
            True

        self._name = name

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this CreateLinkedFile.  # noqa: E501

        The URL of the thumbnail, if the integration provided it.  # noqa: E501

        :return: The thumbnail_url of this CreateLinkedFile.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this CreateLinkedFile.

        The URL of the thumbnail, if the integration provided it.  # noqa: E501

        :param thumbnail_url: The thumbnail_url of this CreateLinkedFile.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def type(self):
        """Gets the type of this CreateLinkedFile.  # noqa: E501

        The integration type of the file (e.g. google, dropbox, box).  # noqa: E501

        :return: The type of this CreateLinkedFile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateLinkedFile.

        The integration type of the file (e.g. google, dropbox, box).  # noqa: E501

        :param type: The type of this CreateLinkedFile.  # noqa: E501
        :type: str
        """
        if type is None:
            # This should not be here...
            True
        allowed_values = ["google", "url", "dropbox", "box", "onedrive"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def size(self):
        """Gets the size of this CreateLinkedFile.  # noqa: E501

        The filesize, if the integration provided it.  # noqa: E501

        :return: The size of this CreateLinkedFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateLinkedFile.

        The filesize, if the integration provided it.  # noqa: E501

        :param size: The size of this CreateLinkedFile.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def uploader_id(self):
        """Gets the uploader_id of this CreateLinkedFile.  # noqa: E501

        The UUID of the member that uploaded the file.  # noqa: E501

        :return: The uploader_id of this CreateLinkedFile.  # noqa: E501
        :rtype: str
        """
        return self._uploader_id

    @uploader_id.setter
    def uploader_id(self, uploader_id):
        """Sets the uploader_id of this CreateLinkedFile.

        The UUID of the member that uploaded the file.  # noqa: E501

        :param uploader_id: The uploader_id of this CreateLinkedFile.  # noqa: E501
        :type: str
        """

        self._uploader_id = uploader_id

    @property
    def content_type(self):
        """Gets the content_type of this CreateLinkedFile.  # noqa: E501

        The content type of the image (e.g. txt/plain).  # noqa: E501

        :return: The content_type of this CreateLinkedFile.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CreateLinkedFile.

        The content type of the image (e.g. txt/plain).  # noqa: E501

        :param content_type: The content_type of this CreateLinkedFile.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def url(self):
        """Gets the url of this CreateLinkedFile.  # noqa: E501

        The URL of linked file.  # noqa: E501

        :return: The url of this CreateLinkedFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateLinkedFile.

        The URL of linked file.  # noqa: E501

        :param url: The url of this CreateLinkedFile.  # noqa: E501
        :type: str
        """
        if url is None:
            # This should not be here...
            True

        self._url = url

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
        if issubclass(CreateLinkedFile, dict):
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
        if not isinstance(other, CreateLinkedFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
