# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V2paymentsProcessingInformationIssuer(object):
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
        'discretionary_data': 'str'
    }

    attribute_map = {
        'discretionary_data': 'discretionaryData'
    }

    def __init__(self, discretionary_data=None):
        """
        V2paymentsProcessingInformationIssuer - a model defined in Swagger
        """

        self._discretionary_data = None

        if discretionary_data is not None:
          self.discretionary_data = discretionary_data

    @property
    def discretionary_data(self):
        """
        Gets the discretionary_data of this V2paymentsProcessingInformationIssuer.
        Data defined by the issuer. The value for this reply field will probably be the same as the value that you submitted in the authorization request, but it is possible for the processor, issuer, or acquirer to modify the value.  This field is supported only for Visa transactions on **CyberSource through VisaNet**. 

        :return: The discretionary_data of this V2paymentsProcessingInformationIssuer.
        :rtype: str
        """
        return self._discretionary_data

    @discretionary_data.setter
    def discretionary_data(self, discretionary_data):
        """
        Sets the discretionary_data of this V2paymentsProcessingInformationIssuer.
        Data defined by the issuer. The value for this reply field will probably be the same as the value that you submitted in the authorization request, but it is possible for the processor, issuer, or acquirer to modify the value.  This field is supported only for Visa transactions on **CyberSource through VisaNet**. 

        :param discretionary_data: The discretionary_data of this V2paymentsProcessingInformationIssuer.
        :type: str
        """
        if discretionary_data is not None and len(discretionary_data) > 255:
            raise ValueError("Invalid value for `discretionary_data`, length must be less than or equal to `255`")

        self._discretionary_data = discretionary_data

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
        if not isinstance(other, V2paymentsProcessingInformationIssuer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other