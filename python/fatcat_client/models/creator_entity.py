# coding: utf-8

"""
    fatcat

    A scalable, versioned, API-oriented catalog of bibliographic entities and file metadata  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreatorEntity(object):
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
        'orcid': 'str',
        'full_name': 'str',
        'state': 'str',
        'ident': 'str',
        'revision': 'int',
        'redirect': 'str',
        'editgroup_id': 'int',
        'extra': 'object'
    }

    attribute_map = {
        'orcid': 'orcid',
        'full_name': 'full_name',
        'state': 'state',
        'ident': 'ident',
        'revision': 'revision',
        'redirect': 'redirect',
        'editgroup_id': 'editgroup_id',
        'extra': 'extra'
    }

    def __init__(self, orcid=None, full_name=None, state=None, ident=None, revision=None, redirect=None, editgroup_id=None, extra=None):  # noqa: E501
        """CreatorEntity - a model defined in Swagger"""  # noqa: E501

        self._orcid = None
        self._full_name = None
        self._state = None
        self._ident = None
        self._revision = None
        self._redirect = None
        self._editgroup_id = None
        self._extra = None
        self.discriminator = None

        if orcid is not None:
            self.orcid = orcid
        self.full_name = full_name
        if state is not None:
            self.state = state
        if ident is not None:
            self.ident = ident
        if revision is not None:
            self.revision = revision
        if redirect is not None:
            self.redirect = redirect
        if editgroup_id is not None:
            self.editgroup_id = editgroup_id
        if extra is not None:
            self.extra = extra

    @property
    def orcid(self):
        """Gets the orcid of this CreatorEntity.  # noqa: E501


        :return: The orcid of this CreatorEntity.  # noqa: E501
        :rtype: str
        """
        return self._orcid

    @orcid.setter
    def orcid(self, orcid):
        """Sets the orcid of this CreatorEntity.


        :param orcid: The orcid of this CreatorEntity.  # noqa: E501
        :type: str
        """

        self._orcid = orcid

    @property
    def full_name(self):
        """Gets the full_name of this CreatorEntity.  # noqa: E501


        :return: The full_name of this CreatorEntity.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this CreatorEntity.


        :param full_name: The full_name of this CreatorEntity.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def state(self):
        """Gets the state of this CreatorEntity.  # noqa: E501


        :return: The state of this CreatorEntity.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreatorEntity.


        :param state: The state of this CreatorEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["wip", "active", "redirect", "deleted"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def ident(self):
        """Gets the ident of this CreatorEntity.  # noqa: E501


        :return: The ident of this CreatorEntity.  # noqa: E501
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident):
        """Sets the ident of this CreatorEntity.


        :param ident: The ident of this CreatorEntity.  # noqa: E501
        :type: str
        """

        self._ident = ident

    @property
    def revision(self):
        """Gets the revision of this CreatorEntity.  # noqa: E501


        :return: The revision of this CreatorEntity.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this CreatorEntity.


        :param revision: The revision of this CreatorEntity.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def redirect(self):
        """Gets the redirect of this CreatorEntity.  # noqa: E501


        :return: The redirect of this CreatorEntity.  # noqa: E501
        :rtype: str
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this CreatorEntity.


        :param redirect: The redirect of this CreatorEntity.  # noqa: E501
        :type: str
        """

        self._redirect = redirect

    @property
    def editgroup_id(self):
        """Gets the editgroup_id of this CreatorEntity.  # noqa: E501


        :return: The editgroup_id of this CreatorEntity.  # noqa: E501
        :rtype: int
        """
        return self._editgroup_id

    @editgroup_id.setter
    def editgroup_id(self, editgroup_id):
        """Sets the editgroup_id of this CreatorEntity.


        :param editgroup_id: The editgroup_id of this CreatorEntity.  # noqa: E501
        :type: int
        """

        self._editgroup_id = editgroup_id

    @property
    def extra(self):
        """Gets the extra of this CreatorEntity.  # noqa: E501


        :return: The extra of this CreatorEntity.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this CreatorEntity.


        :param extra: The extra of this CreatorEntity.  # noqa: E501
        :type: object
        """

        self._extra = extra

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatorEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other