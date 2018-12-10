# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server.models.tapi_common_local_class import TapiCommonLocalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server import util


class TapiOamMip(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, local_id=None, layer_protocol_name=None):  # noqa: E501
        """TapiOamMip - a model defined in OpenAPI

        :param name: The name of this TapiOamMip.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param local_id: The local_id of this TapiOamMip.  # noqa: E501
        :type local_id: str
        :param layer_protocol_name: The layer_protocol_name of this TapiOamMip.  # noqa: E501
        :type layer_protocol_name: TapiCommonLayerProtocolName
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'local_id': str,
            'layer_protocol_name': TapiCommonLayerProtocolName
        }

        self.attribute_map = {
            'name': 'name',
            'local_id': 'local-id',
            'layer_protocol_name': 'layer-protocol-name'
        }

        self._name = name
        self._local_id = local_id
        self._layer_protocol_name = layer_protocol_name

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamMip':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.Mip of this TapiOamMip.  # noqa: E501
        :rtype: TapiOamMip
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiOamMip.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiOamMip.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiOamMip.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiOamMip.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def local_id(self):
        """Gets the local_id of this TapiOamMip.

        none  # noqa: E501

        :return: The local_id of this TapiOamMip.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this TapiOamMip.

        none  # noqa: E501

        :param local_id: The local_id of this TapiOamMip.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def layer_protocol_name(self):
        """Gets the layer_protocol_name of this TapiOamMip.


        :return: The layer_protocol_name of this TapiOamMip.
        :rtype: TapiCommonLayerProtocolName
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name):
        """Sets the layer_protocol_name of this TapiOamMip.


        :param layer_protocol_name: The layer_protocol_name of this TapiOamMip.
        :type layer_protocol_name: TapiCommonLayerProtocolName
        """

        self._layer_protocol_name = layer_protocol_name