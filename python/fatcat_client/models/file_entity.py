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

from fatcat_client.models.file_entity_urls import FileEntityUrls  # noqa: F401,E501


class FileEntity(object):
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
        'releases': 'list[str]',
        'mimetype': 'str',
        'urls': 'list[FileEntityUrls]',
        'sha256': 'str',
        'sha1': 'str',
        'md5': 'str',
        'size': 'int',
        'edit_extra': 'object',
        'extra': 'object',
        'redirect': 'str',
        'revision': 'str',
        'ident': 'str',
        'state': 'str'
    }

    attribute_map = {
        'releases': 'releases',
        'mimetype': 'mimetype',
        'urls': 'urls',
        'sha256': 'sha256',
        'sha1': 'sha1',
        'md5': 'md5',
        'size': 'size',
        'edit_extra': 'edit_extra',
        'extra': 'extra',
        'redirect': 'redirect',
        'revision': 'revision',
        'ident': 'ident',
        'state': 'state'
    }

    def __init__(self, releases=None, mimetype=None, urls=None, sha256=None, sha1=None, md5=None, size=None, edit_extra=None, extra=None, redirect=None, revision=None, ident=None, state=None):  # noqa: E501
        """FileEntity - a model defined in Swagger"""  # noqa: E501

        self._releases = None
        self._mimetype = None
        self._urls = None
        self._sha256 = None
        self._sha1 = None
        self._md5 = None
        self._size = None
        self._edit_extra = None
        self._extra = None
        self._redirect = None
        self._revision = None
        self._ident = None
        self._state = None
        self.discriminator = None

        if releases is not None:
            self.releases = releases
        if mimetype is not None:
            self.mimetype = mimetype
        if urls is not None:
            self.urls = urls
        if sha256 is not None:
            self.sha256 = sha256
        if sha1 is not None:
            self.sha1 = sha1
        if md5 is not None:
            self.md5 = md5
        if size is not None:
            self.size = size
        if edit_extra is not None:
            self.edit_extra = edit_extra
        if extra is not None:
            self.extra = extra
        if redirect is not None:
            self.redirect = redirect
        if revision is not None:
            self.revision = revision
        if ident is not None:
            self.ident = ident
        if state is not None:
            self.state = state

    @property
    def releases(self):
        """Gets the releases of this FileEntity.  # noqa: E501


        :return: The releases of this FileEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this FileEntity.


        :param releases: The releases of this FileEntity.  # noqa: E501
        :type: list[str]
        """

        self._releases = releases

    @property
    def mimetype(self):
        """Gets the mimetype of this FileEntity.  # noqa: E501


        :return: The mimetype of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._mimetype

    @mimetype.setter
    def mimetype(self, mimetype):
        """Sets the mimetype of this FileEntity.


        :param mimetype: The mimetype of this FileEntity.  # noqa: E501
        :type: str
        """

        self._mimetype = mimetype

    @property
    def urls(self):
        """Gets the urls of this FileEntity.  # noqa: E501


        :return: The urls of this FileEntity.  # noqa: E501
        :rtype: list[FileEntityUrls]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this FileEntity.


        :param urls: The urls of this FileEntity.  # noqa: E501
        :type: list[FileEntityUrls]
        """

        self._urls = urls

    @property
    def sha256(self):
        """Gets the sha256 of this FileEntity.  # noqa: E501


        :return: The sha256 of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this FileEntity.


        :param sha256: The sha256 of this FileEntity.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def sha1(self):
        """Gets the sha1 of this FileEntity.  # noqa: E501


        :return: The sha1 of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FileEntity.


        :param sha1: The sha1 of this FileEntity.  # noqa: E501
        :type: str
        """

        self._sha1 = sha1

    @property
    def md5(self):
        """Gets the md5 of this FileEntity.  # noqa: E501


        :return: The md5 of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this FileEntity.


        :param md5: The md5 of this FileEntity.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def size(self):
        """Gets the size of this FileEntity.  # noqa: E501


        :return: The size of this FileEntity.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileEntity.


        :param size: The size of this FileEntity.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def edit_extra(self):
        """Gets the edit_extra of this FileEntity.  # noqa: E501


        :return: The edit_extra of this FileEntity.  # noqa: E501
        :rtype: object
        """
        return self._edit_extra

    @edit_extra.setter
    def edit_extra(self, edit_extra):
        """Sets the edit_extra of this FileEntity.


        :param edit_extra: The edit_extra of this FileEntity.  # noqa: E501
        :type: object
        """

        self._edit_extra = edit_extra

    @property
    def extra(self):
        """Gets the extra of this FileEntity.  # noqa: E501


        :return: The extra of this FileEntity.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this FileEntity.


        :param extra: The extra of this FileEntity.  # noqa: E501
        :type: object
        """

        self._extra = extra

    @property
    def redirect(self):
        """Gets the redirect of this FileEntity.  # noqa: E501

        base32-encoded unique identifier  # noqa: E501

        :return: The redirect of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this FileEntity.

        base32-encoded unique identifier  # noqa: E501

        :param redirect: The redirect of this FileEntity.  # noqa: E501
        :type: str
        """
        if redirect is not None and len(redirect) > 26:
            raise ValueError("Invalid value for `redirect`, length must be less than or equal to `26`")  # noqa: E501
        if redirect is not None and len(redirect) < 26:
            raise ValueError("Invalid value for `redirect`, length must be greater than or equal to `26`")  # noqa: E501
        if redirect is not None and not re.search('[a-zA-Z2-7]{26}', redirect):  # noqa: E501
            raise ValueError("Invalid value for `redirect`, must be a follow pattern or equal to `/[a-zA-Z2-7]{26}/`")  # noqa: E501

        self._redirect = redirect

    @property
    def revision(self):
        """Gets the revision of this FileEntity.  # noqa: E501

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :return: The revision of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this FileEntity.

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :param revision: The revision of this FileEntity.  # noqa: E501
        :type: str
        """
        if revision is not None and len(revision) > 36:
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `36`")  # noqa: E501
        if revision is not None and len(revision) < 36:
            raise ValueError("Invalid value for `revision`, length must be greater than or equal to `36`")  # noqa: E501
        if revision is not None and not re.search('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', revision):  # noqa: E501
            raise ValueError("Invalid value for `revision`, must be a follow pattern or equal to `/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/`")  # noqa: E501

        self._revision = revision

    @property
    def ident(self):
        """Gets the ident of this FileEntity.  # noqa: E501

        base32-encoded unique identifier  # noqa: E501

        :return: The ident of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident):
        """Sets the ident of this FileEntity.

        base32-encoded unique identifier  # noqa: E501

        :param ident: The ident of this FileEntity.  # noqa: E501
        :type: str
        """
        if ident is not None and len(ident) > 26:
            raise ValueError("Invalid value for `ident`, length must be less than or equal to `26`")  # noqa: E501
        if ident is not None and len(ident) < 26:
            raise ValueError("Invalid value for `ident`, length must be greater than or equal to `26`")  # noqa: E501
        if ident is not None and not re.search('[a-zA-Z2-7]{26}', ident):  # noqa: E501
            raise ValueError("Invalid value for `ident`, must be a follow pattern or equal to `/[a-zA-Z2-7]{26}/`")  # noqa: E501

        self._ident = ident

    @property
    def state(self):
        """Gets the state of this FileEntity.  # noqa: E501


        :return: The state of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FileEntity.


        :param state: The state of this FileEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["wip", "active", "redirect", "deleted"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, FileEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
