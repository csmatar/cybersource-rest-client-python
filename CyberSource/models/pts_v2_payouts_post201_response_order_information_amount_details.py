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


class PtsV2PayoutsPost201ResponseOrderInformationAmountDetails(object):
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
        'total_amount': 'str',
        'currency': 'str',
        'settlement_amount': 'str',
        'settlement_currency': 'str'
    }

    attribute_map = {
        'total_amount': 'totalAmount',
        'currency': 'currency',
        'settlement_amount': 'settlementAmount',
        'settlement_currency': 'settlementCurrency'
    }

    def __init__(self, total_amount=None, currency=None, settlement_amount=None, settlement_currency=None):
        """
        PtsV2PayoutsPost201ResponseOrderInformationAmountDetails - a model defined in Swagger
        """

        self._total_amount = None
        self._currency = None
        self._settlement_amount = None
        self._settlement_currency = None

        if total_amount is not None:
          self.total_amount = total_amount
        if currency is not None:
          self.currency = currency
        if settlement_amount is not None:
          self.settlement_amount = settlement_amount
        if settlement_currency is not None:
          self.settlement_currency = settlement_currency

    @property
    def total_amount(self):
        """
        Gets the total_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. This information is covered in:  Table 15, \"Authorization Information for Specific Processors,\" on page 43  Table 19, \"Capture Information for Specific Processors,\" on page 58  Table 23, \"Credit Information for Specific Processors,\" on page 75 If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. See \"Zero Amount Authorizations,\" page 247.  **DCC with a Third-Party Provider**\\ Set this field to the converted amount that was returned by the DCC provider. You must include either this field or offer0 and the offerlevel field amount in your request. For details, see \"Dynamic Currency Conversion with a Third Party Provider,\" page 125.  **FDMS South**\\ If you accept IDR or CLP currencies, see the entry for FDMS South in Table 15, \"Authorization Information for Specific Processors,\" on page 43.  **DCC for First Data**\\ Not used. 

        :return: The total_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. This information is covered in:  Table 15, \"Authorization Information for Specific Processors,\" on page 43  Table 19, \"Capture Information for Specific Processors,\" on page 58  Table 23, \"Credit Information for Specific Processors,\" on page 75 If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. See \"Zero Amount Authorizations,\" page 247.  **DCC with a Third-Party Provider**\\ Set this field to the converted amount that was returned by the DCC provider. You must include either this field or offer0 and the offerlevel field amount in your request. For details, see \"Dynamic Currency Conversion with a Third Party Provider,\" page 125.  **FDMS South**\\ If you accept IDR or CLP currencies, see the entry for FDMS South in Table 15, \"Authorization Information for Specific Processors,\" on page 43.  **DCC for First Data**\\ Not used. 

        :param total_amount: The total_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :type: str
        """
        if total_amount is not None and len(total_amount) > 19:
            raise ValueError("Invalid value for `total_amount`, length must be less than or equal to `19`")

        self._total_amount = total_amount

    @property
    def currency(self):
        """
        Gets the currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes.  For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your request for Payment API.  **DCC for First Data**\\ Your local currency. For details, see \"Dynamic Currency Conversion for First Data,\" page 113. 

        :return: The currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes.  For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your request for Payment API.  **DCC for First Data**\\ Your local currency. For details, see \"Dynamic Currency Conversion for First Data,\" page 113. 

        :param currency: The currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")

        self._currency = currency

    @property
    def settlement_amount(self):
        """
        Gets the settlement_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder’s account. 

        :return: The settlement_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, settlement_amount):
        """
        Sets the settlement_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder’s account. 

        :param settlement_amount: The settlement_amount of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :type: str
        """
        if settlement_amount is not None and len(settlement_amount) > 12:
            raise ValueError("Invalid value for `settlement_amount`, length must be less than or equal to `12`")

        self._settlement_amount = settlement_amount

    @property
    def settlement_currency(self):
        """
        Gets the settlement_currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. 

        :return: The settlement_currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """
        Sets the settlement_currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. 

        :param settlement_currency: The settlement_currency of this PtsV2PayoutsPost201ResponseOrderInformationAmountDetails.
        :type: str
        """
        if settlement_currency is not None and len(settlement_currency) > 3:
            raise ValueError("Invalid value for `settlement_currency`, length must be less than or equal to `3`")

        self._settlement_currency = settlement_currency

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
        if not isinstance(other, PtsV2PayoutsPost201ResponseOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
