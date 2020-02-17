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


class RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation(object):
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
        'ip_country_confidence': 'int',
        'info_codes': 'list[str]',
        'watch_list': 'RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformationWatchList'
    }

    attribute_map = {
        'ip_country_confidence': 'ipCountryConfidence',
        'info_codes': 'infoCodes',
        'watch_list': 'watchList'
    }

    def __init__(self, ip_country_confidence=None, info_codes=None, watch_list=None):
        """
        RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation - a model defined in Swagger
        """

        self._ip_country_confidence = None
        self._info_codes = None
        self._watch_list = None

        if ip_country_confidence is not None:
          self.ip_country_confidence = ip_country_confidence
        if info_codes is not None:
          self.info_codes = info_codes
        if watch_list is not None:
          self.watch_list = watch_list

    @property
    def ip_country_confidence(self):
        """
        Gets the ip_country_confidence of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        Likelihood that the country associated with the customer’s IP address was identified correctly. Returns a value from 1–100, where 100 indicates the highest likelihood. If the country cannot be determined, the value is –1. 

        :return: The ip_country_confidence of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        :rtype: int
        """
        return self._ip_country_confidence

    @ip_country_confidence.setter
    def ip_country_confidence(self, ip_country_confidence):
        """
        Sets the ip_country_confidence of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        Likelihood that the country associated with the customer’s IP address was identified correctly. Returns a value from 1–100, where 100 indicates the highest likelihood. If the country cannot be determined, the value is –1. 

        :param ip_country_confidence: The ip_country_confidence of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        :type: int
        """
        if ip_country_confidence is not None and ip_country_confidence > 100:
            raise ValueError("Invalid value for `ip_country_confidence`, must be a value less than or equal to `100`")
        if ip_country_confidence is not None and ip_country_confidence < -1:
            raise ValueError("Invalid value for `ip_country_confidence`, must be a value greater than or equal to `-1`")

        self._ip_country_confidence = ip_country_confidence

    @property
    def info_codes(self):
        """
        Gets the info_codes of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        Returned when the Denied Parties List check (first two codes) or the export service (all others) would have declined the transaction. This field can contain one or more of these values: - `MATCH-DPC`: Denied Parties List match. - `UNV-DPC`: Denied Parties List unavailable. - `MATCH-BCO`: Billing country restricted. - `MATCH-EMCO`: Email country restricted. - `MATCH-HCO`: Host name country restricted. - `MATCH-IPCO`: IP country restricted. - `MATCH-SCO`: Shipping country restricted. 

        :return: The info_codes of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        :rtype: list[str]
        """
        return self._info_codes

    @info_codes.setter
    def info_codes(self, info_codes):
        """
        Sets the info_codes of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        Returned when the Denied Parties List check (first two codes) or the export service (all others) would have declined the transaction. This field can contain one or more of these values: - `MATCH-DPC`: Denied Parties List match. - `UNV-DPC`: Denied Parties List unavailable. - `MATCH-BCO`: Billing country restricted. - `MATCH-EMCO`: Email country restricted. - `MATCH-HCO`: Host name country restricted. - `MATCH-IPCO`: IP country restricted. - `MATCH-SCO`: Shipping country restricted. 

        :param info_codes: The info_codes of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        :type: list[str]
        """

        self._info_codes = info_codes

    @property
    def watch_list(self):
        """
        Gets the watch_list of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.

        :return: The watch_list of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        :rtype: RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformationWatchList
        """
        return self._watch_list

    @watch_list.setter
    def watch_list(self, watch_list):
        """
        Sets the watch_list of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.

        :param watch_list: The watch_list of this RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.
        :type: RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformationWatchList
        """

        self._watch_list = watch_list

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
        if not isinstance(other, RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
