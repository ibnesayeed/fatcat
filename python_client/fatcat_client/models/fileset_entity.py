# coding: utf-8

"""
    fatcat

    A scalable, versioned, API-oriented catalog of bibliographic entities and file metadata  # noqa: E501

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from fatcat_client.models.fileset_file import FilesetFile  # noqa: F401,E501
from fatcat_client.models.fileset_url import FilesetUrl  # noqa: F401,E501
from fatcat_client.models.release_entity import ReleaseEntity  # noqa: F401,E501


class FilesetEntity(object):
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
        'releases': 'list[ReleaseEntity]',
        'release_ids': 'list[str]',
        'urls': 'list[FilesetUrl]',
        'manifest': 'list[FilesetFile]',
        'state': 'str',
        'ident': 'str',
        'revision': 'str',
        'redirect': 'str',
        'extra': 'object',
        'edit_extra': 'object'
    }

    attribute_map = {
        'releases': 'releases',
        'release_ids': 'release_ids',
        'urls': 'urls',
        'manifest': 'manifest',
        'state': 'state',
        'ident': 'ident',
        'revision': 'revision',
        'redirect': 'redirect',
        'extra': 'extra',
        'edit_extra': 'edit_extra'
    }

    def __init__(self, releases=None, release_ids=None, urls=None, manifest=None, state=None, ident=None, revision=None, redirect=None, extra=None, edit_extra=None):  # noqa: E501
        """FilesetEntity - a model defined in Swagger"""  # noqa: E501

        self._releases = None
        self._release_ids = None
        self._urls = None
        self._manifest = None
        self._state = None
        self._ident = None
        self._revision = None
        self._redirect = None
        self._extra = None
        self._edit_extra = None
        self.discriminator = None

        if releases is not None:
            self.releases = releases
        if release_ids is not None:
            self.release_ids = release_ids
        if urls is not None:
            self.urls = urls
        if manifest is not None:
            self.manifest = manifest
        if state is not None:
            self.state = state
        if ident is not None:
            self.ident = ident
        if revision is not None:
            self.revision = revision
        if redirect is not None:
            self.redirect = redirect
        if extra is not None:
            self.extra = extra
        if edit_extra is not None:
            self.edit_extra = edit_extra

    @property
    def releases(self):
        """Gets the releases of this FilesetEntity.  # noqa: E501

        Optional; GET-only  # noqa: E501

        :return: The releases of this FilesetEntity.  # noqa: E501
        :rtype: list[ReleaseEntity]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this FilesetEntity.

        Optional; GET-only  # noqa: E501

        :param releases: The releases of this FilesetEntity.  # noqa: E501
        :type: list[ReleaseEntity]
        """

        self._releases = releases

    @property
    def release_ids(self):
        """Gets the release_ids of this FilesetEntity.  # noqa: E501


        :return: The release_ids of this FilesetEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._release_ids

    @release_ids.setter
    def release_ids(self, release_ids):
        """Sets the release_ids of this FilesetEntity.


        :param release_ids: The release_ids of this FilesetEntity.  # noqa: E501
        :type: list[str]
        """

        self._release_ids = release_ids

    @property
    def urls(self):
        """Gets the urls of this FilesetEntity.  # noqa: E501


        :return: The urls of this FilesetEntity.  # noqa: E501
        :rtype: list[FilesetUrl]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this FilesetEntity.


        :param urls: The urls of this FilesetEntity.  # noqa: E501
        :type: list[FilesetUrl]
        """

        self._urls = urls

    @property
    def manifest(self):
        """Gets the manifest of this FilesetEntity.  # noqa: E501


        :return: The manifest of this FilesetEntity.  # noqa: E501
        :rtype: list[FilesetFile]
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this FilesetEntity.


        :param manifest: The manifest of this FilesetEntity.  # noqa: E501
        :type: list[FilesetFile]
        """

        self._manifest = manifest

    @property
    def state(self):
        """Gets the state of this FilesetEntity.  # noqa: E501


        :return: The state of this FilesetEntity.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FilesetEntity.


        :param state: The state of this FilesetEntity.  # noqa: E501
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
        """Gets the ident of this FilesetEntity.  # noqa: E501

        base32-encoded unique identifier  # noqa: E501

        :return: The ident of this FilesetEntity.  # noqa: E501
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident):
        """Sets the ident of this FilesetEntity.

        base32-encoded unique identifier  # noqa: E501

        :param ident: The ident of this FilesetEntity.  # noqa: E501
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
    def revision(self):
        """Gets the revision of this FilesetEntity.  # noqa: E501

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :return: The revision of this FilesetEntity.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this FilesetEntity.

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :param revision: The revision of this FilesetEntity.  # noqa: E501
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
    def redirect(self):
        """Gets the redirect of this FilesetEntity.  # noqa: E501

        base32-encoded unique identifier  # noqa: E501

        :return: The redirect of this FilesetEntity.  # noqa: E501
        :rtype: str
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this FilesetEntity.

        base32-encoded unique identifier  # noqa: E501

        :param redirect: The redirect of this FilesetEntity.  # noqa: E501
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
    def extra(self):
        """Gets the extra of this FilesetEntity.  # noqa: E501


        :return: The extra of this FilesetEntity.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this FilesetEntity.


        :param extra: The extra of this FilesetEntity.  # noqa: E501
        :type: object
        """

        self._extra = extra

    @property
    def edit_extra(self):
        """Gets the edit_extra of this FilesetEntity.  # noqa: E501


        :return: The edit_extra of this FilesetEntity.  # noqa: E501
        :rtype: object
        """
        return self._edit_extra

    @edit_extra.setter
    def edit_extra(self, edit_extra):
        """Sets the edit_extra of this FilesetEntity.


        :param edit_extra: The edit_extra of this FilesetEntity.  # noqa: E501
        :type: object
        """

        self._edit_extra = edit_extra

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
        if not isinstance(other, FilesetEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
