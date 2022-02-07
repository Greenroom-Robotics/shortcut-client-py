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

class EpicStats(object):
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
        'num_points_done': 'int',
        'num_related_documents': 'int',
        'average_cycle_time': 'int',
        'num_stories_unstarted': 'int',
        'num_stories_total': 'int',
        'last_story_update': 'datetime',
        'num_points_started': 'int',
        'num_points_unstarted': 'int',
        'num_stories_started': 'int',
        'num_stories_unestimated': 'int',
        'average_lead_time': 'int',
        'num_points': 'int',
        'num_stories_done': 'int'
    }

    attribute_map = {
        'num_points_done': 'num_points_done',
        'num_related_documents': 'num_related_documents',
        'average_cycle_time': 'average_cycle_time',
        'num_stories_unstarted': 'num_stories_unstarted',
        'num_stories_total': 'num_stories_total',
        'last_story_update': 'last_story_update',
        'num_points_started': 'num_points_started',
        'num_points_unstarted': 'num_points_unstarted',
        'num_stories_started': 'num_stories_started',
        'num_stories_unestimated': 'num_stories_unestimated',
        'average_lead_time': 'average_lead_time',
        'num_points': 'num_points',
        'num_stories_done': 'num_stories_done'
    }

    def __init__(self, num_points_done=None, num_related_documents=None, average_cycle_time=None, num_stories_unstarted=None, num_stories_total=None, last_story_update=None, num_points_started=None, num_points_unstarted=None, num_stories_started=None, num_stories_unestimated=None, average_lead_time=None, num_points=None, num_stories_done=None):  # noqa: E501
        """EpicStats - a model defined in Swagger"""  # noqa: E501
        self._num_points_done = None
        self._num_related_documents = None
        self._average_cycle_time = None
        self._num_stories_unstarted = None
        self._num_stories_total = None
        self._last_story_update = None
        self._num_points_started = None
        self._num_points_unstarted = None
        self._num_stories_started = None
        self._num_stories_unestimated = None
        self._average_lead_time = None
        self._num_points = None
        self._num_stories_done = None
        self.discriminator = None
        self.num_points_done = num_points_done
        self.num_related_documents = num_related_documents
        if average_cycle_time is not None:
            self.average_cycle_time = average_cycle_time
        self.num_stories_unstarted = num_stories_unstarted
        self.num_stories_total = num_stories_total
        self.last_story_update = last_story_update
        self.num_points_started = num_points_started
        self.num_points_unstarted = num_points_unstarted
        self.num_stories_started = num_stories_started
        self.num_stories_unestimated = num_stories_unestimated
        if average_lead_time is not None:
            self.average_lead_time = average_lead_time
        self.num_points = num_points
        self.num_stories_done = num_stories_done

    @property
    def num_points_done(self):
        """Gets the num_points_done of this EpicStats.  # noqa: E501

        The total number of completed points in this Epic.  # noqa: E501

        :return: The num_points_done of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_points_done

    @num_points_done.setter
    def num_points_done(self, num_points_done):
        """Sets the num_points_done of this EpicStats.

        The total number of completed points in this Epic.  # noqa: E501

        :param num_points_done: The num_points_done of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_points_done is None:
            # This should not be here...
            True

        self._num_points_done = num_points_done

    @property
    def num_related_documents(self):
        """Gets the num_related_documents of this EpicStats.  # noqa: E501

        The total number of documents associated with this Epic.  # noqa: E501

        :return: The num_related_documents of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_related_documents

    @num_related_documents.setter
    def num_related_documents(self, num_related_documents):
        """Sets the num_related_documents of this EpicStats.

        The total number of documents associated with this Epic.  # noqa: E501

        :param num_related_documents: The num_related_documents of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_related_documents is None:
            # This should not be here...
            True

        self._num_related_documents = num_related_documents

    @property
    def average_cycle_time(self):
        """Gets the average_cycle_time of this EpicStats.  # noqa: E501

        The average cycle time (in seconds) of completed stories in this Epic.  # noqa: E501

        :return: The average_cycle_time of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._average_cycle_time

    @average_cycle_time.setter
    def average_cycle_time(self, average_cycle_time):
        """Sets the average_cycle_time of this EpicStats.

        The average cycle time (in seconds) of completed stories in this Epic.  # noqa: E501

        :param average_cycle_time: The average_cycle_time of this EpicStats.  # noqa: E501
        :type: int
        """

        self._average_cycle_time = average_cycle_time

    @property
    def num_stories_unstarted(self):
        """Gets the num_stories_unstarted of this EpicStats.  # noqa: E501

        The total number of unstarted Stories in this Epic.  # noqa: E501

        :return: The num_stories_unstarted of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_stories_unstarted

    @num_stories_unstarted.setter
    def num_stories_unstarted(self, num_stories_unstarted):
        """Sets the num_stories_unstarted of this EpicStats.

        The total number of unstarted Stories in this Epic.  # noqa: E501

        :param num_stories_unstarted: The num_stories_unstarted of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_stories_unstarted is None:
            # This should not be here...
            True

        self._num_stories_unstarted = num_stories_unstarted

    @property
    def num_stories_total(self):
        """Gets the num_stories_total of this EpicStats.  # noqa: E501

        The total number of Stories in this Epic.  # noqa: E501

        :return: The num_stories_total of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_stories_total

    @num_stories_total.setter
    def num_stories_total(self, num_stories_total):
        """Sets the num_stories_total of this EpicStats.

        The total number of Stories in this Epic.  # noqa: E501

        :param num_stories_total: The num_stories_total of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_stories_total is None:
            # This should not be here...
            True

        self._num_stories_total = num_stories_total

    @property
    def last_story_update(self):
        """Gets the last_story_update of this EpicStats.  # noqa: E501

        The date of the last update of a Story in this Epic.  # noqa: E501

        :return: The last_story_update of this EpicStats.  # noqa: E501
        :rtype: datetime
        """
        return self._last_story_update

    @last_story_update.setter
    def last_story_update(self, last_story_update):
        """Sets the last_story_update of this EpicStats.

        The date of the last update of a Story in this Epic.  # noqa: E501

        :param last_story_update: The last_story_update of this EpicStats.  # noqa: E501
        :type: datetime
        """
        if last_story_update is None:
            # This should not be here...
            True

        self._last_story_update = last_story_update

    @property
    def num_points_started(self):
        """Gets the num_points_started of this EpicStats.  # noqa: E501

        The total number of started points in this Epic.  # noqa: E501

        :return: The num_points_started of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_points_started

    @num_points_started.setter
    def num_points_started(self, num_points_started):
        """Sets the num_points_started of this EpicStats.

        The total number of started points in this Epic.  # noqa: E501

        :param num_points_started: The num_points_started of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_points_started is None:
            # This should not be here...
            True

        self._num_points_started = num_points_started

    @property
    def num_points_unstarted(self):
        """Gets the num_points_unstarted of this EpicStats.  # noqa: E501

        The total number of unstarted points in this Epic.  # noqa: E501

        :return: The num_points_unstarted of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_points_unstarted

    @num_points_unstarted.setter
    def num_points_unstarted(self, num_points_unstarted):
        """Sets the num_points_unstarted of this EpicStats.

        The total number of unstarted points in this Epic.  # noqa: E501

        :param num_points_unstarted: The num_points_unstarted of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_points_unstarted is None:
            # This should not be here...
            True

        self._num_points_unstarted = num_points_unstarted

    @property
    def num_stories_started(self):
        """Gets the num_stories_started of this EpicStats.  # noqa: E501

        The total number of started Stories in this Epic.  # noqa: E501

        :return: The num_stories_started of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_stories_started

    @num_stories_started.setter
    def num_stories_started(self, num_stories_started):
        """Sets the num_stories_started of this EpicStats.

        The total number of started Stories in this Epic.  # noqa: E501

        :param num_stories_started: The num_stories_started of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_stories_started is None:
            # This should not be here...
            True

        self._num_stories_started = num_stories_started

    @property
    def num_stories_unestimated(self):
        """Gets the num_stories_unestimated of this EpicStats.  # noqa: E501

        The total number of Stories with no point estimate.  # noqa: E501

        :return: The num_stories_unestimated of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_stories_unestimated

    @num_stories_unestimated.setter
    def num_stories_unestimated(self, num_stories_unestimated):
        """Sets the num_stories_unestimated of this EpicStats.

        The total number of Stories with no point estimate.  # noqa: E501

        :param num_stories_unestimated: The num_stories_unestimated of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_stories_unestimated is None:
            # This should not be here...
            True

        self._num_stories_unestimated = num_stories_unestimated

    @property
    def average_lead_time(self):
        """Gets the average_lead_time of this EpicStats.  # noqa: E501

        The average lead time (in seconds) of completed stories in this Epic.  # noqa: E501

        :return: The average_lead_time of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._average_lead_time

    @average_lead_time.setter
    def average_lead_time(self, average_lead_time):
        """Sets the average_lead_time of this EpicStats.

        The average lead time (in seconds) of completed stories in this Epic.  # noqa: E501

        :param average_lead_time: The average_lead_time of this EpicStats.  # noqa: E501
        :type: int
        """

        self._average_lead_time = average_lead_time

    @property
    def num_points(self):
        """Gets the num_points of this EpicStats.  # noqa: E501

        The total number of points in this Epic.  # noqa: E501

        :return: The num_points of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_points

    @num_points.setter
    def num_points(self, num_points):
        """Sets the num_points of this EpicStats.

        The total number of points in this Epic.  # noqa: E501

        :param num_points: The num_points of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_points is None:
            # This should not be here...
            True

        self._num_points = num_points

    @property
    def num_stories_done(self):
        """Gets the num_stories_done of this EpicStats.  # noqa: E501

        The total number of done Stories in this Epic.  # noqa: E501

        :return: The num_stories_done of this EpicStats.  # noqa: E501
        :rtype: int
        """
        return self._num_stories_done

    @num_stories_done.setter
    def num_stories_done(self, num_stories_done):
        """Sets the num_stories_done of this EpicStats.

        The total number of done Stories in this Epic.  # noqa: E501

        :param num_stories_done: The num_stories_done of this EpicStats.  # noqa: E501
        :type: int
        """
        if num_stories_done is None:
            # This should not be here...
            True

        self._num_stories_done = num_stories_done

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
        if issubclass(EpicStats, dict):
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
        if not isinstance(other, EpicStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
