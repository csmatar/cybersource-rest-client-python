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


class Ptsv2paymentsidMerchantInformation(object):
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
        'transaction_local_date_time': 'str'
    }

    attribute_map = {
        'transaction_local_date_time': 'transactionLocalDateTime'
    }

    def __init__(self, transaction_local_date_time=None):
        """
        Ptsv2paymentsidMerchantInformation - a model defined in Swagger
        """

        self._transaction_local_date_time = None

        if transaction_local_date_time is not None:
          self.transaction_local_date_time = transaction_local_date_time

    @property
    def transaction_local_date_time(self):
        """
        Gets the transaction_local_date_time of this Ptsv2paymentsidMerchantInformation.
        Local date and time at your physical location. Include both the date and time in this field or leave it blank. This field is supported only for **CyberSource through VisaNet**.  For processor-specific information, see the `transaction_local_date_time` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  Format: `YYYYMMDDhhmmss`, where:   - YYYY = year  - MM = month  - DD = day  - hh = hour  - mm = minutes  - ss = seconds   For processor-specific information, see the `transaction_local_date_time` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The transaction_local_date_time of this Ptsv2paymentsidMerchantInformation.
        :rtype: str
        """
        return self._transaction_local_date_time

    @transaction_local_date_time.setter
    def transaction_local_date_time(self, transaction_local_date_time):
        """
        Sets the transaction_local_date_time of this Ptsv2paymentsidMerchantInformation.
        Local date and time at your physical location. Include both the date and time in this field or leave it blank. This field is supported only for **CyberSource through VisaNet**.  For processor-specific information, see the `transaction_local_date_time` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  Format: `YYYYMMDDhhmmss`, where:   - YYYY = year  - MM = month  - DD = day  - hh = hour  - mm = minutes  - ss = seconds   For processor-specific information, see the `transaction_local_date_time` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param transaction_local_date_time: The transaction_local_date_time of this Ptsv2paymentsidMerchantInformation.
        :type: str
        """
        if transaction_local_date_time is not None and len(transaction_local_date_time) > 14:
            raise ValueError("Invalid value for `transaction_local_date_time`, length must be less than or equal to `14`")

        self._transaction_local_date_time = transaction_local_date_time

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
        if not isinstance(other, Ptsv2paymentsidMerchantInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
