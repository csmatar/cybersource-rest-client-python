# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TssV2TransactionsPost201Response(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'search_id': 'str',
        'save': 'bool',
        'name': 'str',
        'timezone': 'str',
        'query': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort': 'str',
        'count': 'int',
        'total_count': 'int',
        'status': 'str',
        'submit_time_utc': 'str',
        'embedded': 'TssV2TransactionsPost201ResponseEmbedded',
        'links': 'PtsV2IncrementalAuthorizationPatch201ResponseLinks'
    }

    attribute_map = {
        'search_id': 'searchId',
        'save': 'save',
        'name': 'name',
        'timezone': 'timezone',
        'query': 'query',
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'count': 'count',
        'total_count': 'totalCount',
        'status': 'status',
        'submit_time_utc': 'submitTimeUtc',
        'embedded': '_embedded',
        'links': '_links'
    }

    def __init__(self, search_id=None, save=None, name=None, timezone=None, query=None, offset=None, limit=None, sort=None, count=None, total_count=None, status=None, submit_time_utc=None, embedded=None, links=None):
        """
        TssV2TransactionsPost201Response - a model defined in Swagger
        """

        self._search_id = None
        self._save = None
        self._name = None
        self._timezone = None
        self._query = None
        self._offset = None
        self._limit = None
        self._sort = None
        self._count = None
        self._total_count = None
        self._status = None
        self._submit_time_utc = None
        self._embedded = None
        self._links = None

        if search_id is not None:
          self.search_id = search_id
        if save is not None:
          self.save = save
        if name is not None:
          self.name = name
        if timezone is not None:
          self.timezone = timezone
        if query is not None:
          self.query = query
        if offset is not None:
          self.offset = offset
        if limit is not None:
          self.limit = limit
        if sort is not None:
          self.sort = sort
        if count is not None:
          self.count = count
        if total_count is not None:
          self.total_count = total_count
        if status is not None:
          self.status = status
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if embedded is not None:
          self.embedded = embedded
        if links is not None:
          self.links = links

    @property
    def search_id(self):
        """
        Gets the search_id of this TssV2TransactionsPost201Response.
        An unique identification number assigned by CyberSource to identify each Search request.

        :return: The search_id of this TssV2TransactionsPost201Response.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """
        Sets the search_id of this TssV2TransactionsPost201Response.
        An unique identification number assigned by CyberSource to identify each Search request.

        :param search_id: The search_id of this TssV2TransactionsPost201Response.
        :type: str
        """
        if search_id is not None and len(search_id) > 60:
            raise ValueError("Invalid value for `search_id`, length must be less than or equal to `60`")

        self._search_id = search_id

    @property
    def save(self):
        """
        Gets the save of this TssV2TransactionsPost201Response.
        save or not save.

        :return: The save of this TssV2TransactionsPost201Response.
        :rtype: bool
        """
        return self._save

    @save.setter
    def save(self, save):
        """
        Sets the save of this TssV2TransactionsPost201Response.
        save or not save.

        :param save: The save of this TssV2TransactionsPost201Response.
        :type: bool
        """

        self._save = save

    @property
    def name(self):
        """
        Gets the name of this TssV2TransactionsPost201Response.
        The description for this field is not available. 

        :return: The name of this TssV2TransactionsPost201Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TssV2TransactionsPost201Response.
        The description for this field is not available. 

        :param name: The name of this TssV2TransactionsPost201Response.
        :type: str
        """

        self._name = name

    @property
    def timezone(self):
        """
        Gets the timezone of this TssV2TransactionsPost201Response.
        Time Zone in ISO format.

        :return: The timezone of this TssV2TransactionsPost201Response.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this TssV2TransactionsPost201Response.
        Time Zone in ISO format.

        :param timezone: The timezone of this TssV2TransactionsPost201Response.
        :type: str
        """

        self._timezone = timezone

    @property
    def query(self):
        """
        Gets the query of this TssV2TransactionsPost201Response.
        transaction search query string.

        :return: The query of this TssV2TransactionsPost201Response.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this TssV2TransactionsPost201Response.
        transaction search query string.

        :param query: The query of this TssV2TransactionsPost201Response.
        :type: str
        """

        self._query = query

    @property
    def offset(self):
        """
        Gets the offset of this TssV2TransactionsPost201Response.
        offset.

        :return: The offset of this TssV2TransactionsPost201Response.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this TssV2TransactionsPost201Response.
        offset.

        :param offset: The offset of this TssV2TransactionsPost201Response.
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """
        Gets the limit of this TssV2TransactionsPost201Response.
        Limit on number of results.

        :return: The limit of this TssV2TransactionsPost201Response.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this TssV2TransactionsPost201Response.
        Limit on number of results.

        :param limit: The limit of this TssV2TransactionsPost201Response.
        :type: int
        """

        self._limit = limit

    @property
    def sort(self):
        """
        Gets the sort of this TssV2TransactionsPost201Response.
        A comma separated list of the following form - fieldName1 asc or desc, fieldName2 asc or desc, etc.

        :return: The sort of this TssV2TransactionsPost201Response.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this TssV2TransactionsPost201Response.
        A comma separated list of the following form - fieldName1 asc or desc, fieldName2 asc or desc, etc.

        :param sort: The sort of this TssV2TransactionsPost201Response.
        :type: str
        """

        self._sort = sort

    @property
    def count(self):
        """
        Gets the count of this TssV2TransactionsPost201Response.
        Results for this page, this could be below the limit.

        :return: The count of this TssV2TransactionsPost201Response.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this TssV2TransactionsPost201Response.
        Results for this page, this could be below the limit.

        :param count: The count of this TssV2TransactionsPost201Response.
        :type: int
        """

        self._count = count

    @property
    def total_count(self):
        """
        Gets the total_count of this TssV2TransactionsPost201Response.
        Total number of results.

        :return: The total_count of this TssV2TransactionsPost201Response.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this TssV2TransactionsPost201Response.
        Total number of results.

        :param total_count: The total_count of this TssV2TransactionsPost201Response.
        :type: int
        """

        self._total_count = total_count

    @property
    def status(self):
        """
        Gets the status of this TssV2TransactionsPost201Response.
        The status of the submitted transaction.

        :return: The status of this TssV2TransactionsPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TssV2TransactionsPost201Response.
        The status of the submitted transaction.

        :param status: The status of this TssV2TransactionsPost201Response.
        :type: str
        """

        self._status = status

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this TssV2TransactionsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :return: The submit_time_utc of this TssV2TransactionsPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this TssV2TransactionsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this TssV2TransactionsPost201Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def embedded(self):
        """
        Gets the embedded of this TssV2TransactionsPost201Response.

        :return: The embedded of this TssV2TransactionsPost201Response.
        :rtype: TssV2TransactionsPost201ResponseEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """
        Sets the embedded of this TssV2TransactionsPost201Response.

        :param embedded: The embedded of this TssV2TransactionsPost201Response.
        :type: TssV2TransactionsPost201ResponseEmbedded
        """

        self._embedded = embedded

    @property
    def links(self):
        """
        Gets the links of this TssV2TransactionsPost201Response.

        :return: The links of this TssV2TransactionsPost201Response.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TssV2TransactionsPost201Response.

        :param links: The links of this TssV2TransactionsPost201Response.
        :type: PtsV2IncrementalAuthorizationPatch201ResponseLinks
        """

        self._links = links

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TssV2TransactionsPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
