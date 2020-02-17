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


class Riskv1authenticationsOrderInformationLineItems(object):
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
        'unit_price': 'str',
        'quantity': 'int',
        'gift_card_currency': 'int',
        'product_sku': 'str',
        'product_description': 'str',
        'product_name': 'str',
        'passenger': 'Riskv1decisionsOrderInformationPassenger',
        'shipping_destination_types': 'str',
        'tax_amount': 'str'
    }

    attribute_map = {
        'total_amount': 'totalAmount',
        'unit_price': 'unitPrice',
        'quantity': 'quantity',
        'gift_card_currency': 'giftCardCurrency',
        'product_sku': 'productSKU',
        'product_description': 'productDescription',
        'product_name': 'productName',
        'passenger': 'passenger',
        'shipping_destination_types': 'shippingDestinationTypes',
        'tax_amount': 'taxAmount'
    }

    def __init__(self, total_amount=None, unit_price=None, quantity=None, gift_card_currency=None, product_sku=None, product_description=None, product_name=None, passenger=None, shipping_destination_types=None, tax_amount=None):
        """
        Riskv1authenticationsOrderInformationLineItems - a model defined in Swagger
        """

        self._total_amount = None
        self._unit_price = None
        self._quantity = None
        self._gift_card_currency = None
        self._product_sku = None
        self._product_description = None
        self._product_name = None
        self._passenger = None
        self._shipping_destination_types = None
        self._tax_amount = None

        if total_amount is not None:
          self.total_amount = total_amount
        self.unit_price = unit_price
        if quantity is not None:
          self.quantity = quantity
        if gift_card_currency is not None:
          self.gift_card_currency = gift_card_currency
        if product_sku is not None:
          self.product_sku = product_sku
        if product_description is not None:
          self.product_description = product_description
        if product_name is not None:
          self.product_name = product_name
        if passenger is not None:
          self.passenger = passenger
        if shipping_destination_types is not None:
          self.shipping_destination_types = shipping_destination_types
        if tax_amount is not None:
          self.tax_amount = tax_amount

    @property
    def total_amount(self):
        """
        Gets the total_amount of this Riskv1authenticationsOrderInformationLineItems.
        Total amount for the item. Normally calculated as the unit price times quantity.  When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the purchase amount total for prepaid gift cards in major units.  Example: 123.45 USD = 123 

        :return: The total_amount of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this Riskv1authenticationsOrderInformationLineItems.
        Total amount for the item. Normally calculated as the unit price times quantity.  When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the purchase amount total for prepaid gift cards in major units.  Example: 123.45 USD = 123 

        :param total_amount: The total_amount of this Riskv1authenticationsOrderInformationLineItems.
        :type: str
        """
        if total_amount is not None and len(total_amount) > 13:
            raise ValueError("Invalid value for `total_amount`, length must be less than or equal to `13`")

        self._total_amount = total_amount

    @property
    def unit_price(self):
        """
        Gets the unit_price of this Riskv1authenticationsOrderInformationLineItems.
        Per-item price of the product. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places.  For processor-specific information, see the `amount` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. See these guides for details: - [Merchant Descriptors Using the SCMP API Guide] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/) - \"Capture Information for Specific Processors\" section in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request. For details, see \"Dynamic Currency Conversion with a Third Party Provider\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. See \"Zero Amount Authorizations\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The unit_price of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this Riskv1authenticationsOrderInformationLineItems.
        Per-item price of the product. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places.  For processor-specific information, see the `amount` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. See these guides for details: - [Merchant Descriptors Using the SCMP API Guide] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/) - \"Capture Information for Specific Processors\" section in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request. For details, see \"Dynamic Currency Conversion with a Third Party Provider\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. See \"Zero Amount Authorizations\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param unit_price: The unit_price of this Riskv1authenticationsOrderInformationLineItems.
        :type: str
        """
        if unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")
        if unit_price is not None and len(unit_price) > 15:
            raise ValueError("Invalid value for `unit_price`, length must be less than or equal to `15`")

        self._unit_price = unit_price

    @property
    def quantity(self):
        """
        Gets the quantity of this Riskv1authenticationsOrderInformationLineItems.
        Number of units for this order.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when _orderInformation.lineItems[].productCode_ is not set to **default** or one of the other values that are related to shipping and/or handling.  When orderInformation.lineItems[].productCode is \"gift_card\", this is the total count of individual prepaid gift cards purchased. 

        :return: The quantity of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Riskv1authenticationsOrderInformationLineItems.
        Number of units for this order.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when _orderInformation.lineItems[].productCode_ is not set to **default** or one of the other values that are related to shipping and/or handling.  When orderInformation.lineItems[].productCode is \"gift_card\", this is the total count of individual prepaid gift cards purchased. 

        :param quantity: The quantity of this Riskv1authenticationsOrderInformationLineItems.
        :type: int
        """
        if quantity is not None and quantity > 999999999:
            raise ValueError("Invalid value for `quantity`, must be a value less than or equal to `999999999`")
        if quantity is not None and quantity < 1:
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")

        self._quantity = quantity

    @property
    def gift_card_currency(self):
        """
        Gets the gift_card_currency of this Riskv1authenticationsOrderInformationLineItems.
        When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the currency used for the gift card purchase.  For details, see `pa_gift_card_currency` field description in [CyberSource Payer Authentication Using the SCMP API.] (https://apps.cybersource.com/library/documentation/dev_guides/Payer_Authentication_SCMP_API/Payer_Authentication_SCMP_API.pdf)  For the possible values, see the [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf) 

        :return: The gift_card_currency of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: int
        """
        return self._gift_card_currency

    @gift_card_currency.setter
    def gift_card_currency(self, gift_card_currency):
        """
        Sets the gift_card_currency of this Riskv1authenticationsOrderInformationLineItems.
        When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the currency used for the gift card purchase.  For details, see `pa_gift_card_currency` field description in [CyberSource Payer Authentication Using the SCMP API.] (https://apps.cybersource.com/library/documentation/dev_guides/Payer_Authentication_SCMP_API/Payer_Authentication_SCMP_API.pdf)  For the possible values, see the [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf) 

        :param gift_card_currency: The gift_card_currency of this Riskv1authenticationsOrderInformationLineItems.
        :type: int
        """

        self._gift_card_currency = gift_card_currency

    @property
    def product_sku(self):
        """
        Gets the product_sku of this Riskv1authenticationsOrderInformationLineItems.
        Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when _orderInformation.lineItems[].productCode_ is not set to **default** or one of the other values that are related to shipping and/or handling. 

        :return: The product_sku of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """
        Sets the product_sku of this Riskv1authenticationsOrderInformationLineItems.
        Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when _orderInformation.lineItems[].productCode_ is not set to **default** or one of the other values that are related to shipping and/or handling. 

        :param product_sku: The product_sku of this Riskv1authenticationsOrderInformationLineItems.
        :type: str
        """
        if product_sku is not None and len(product_sku) > 255:
            raise ValueError("Invalid value for `product_sku`, length must be less than or equal to `255`")

        self._product_sku = product_sku

    @property
    def product_description(self):
        """
        Gets the product_description of this Riskv1authenticationsOrderInformationLineItems.
        Brief description of item.

        :return: The product_description of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """
        Sets the product_description of this Riskv1authenticationsOrderInformationLineItems.
        Brief description of item.

        :param product_description: The product_description of this Riskv1authenticationsOrderInformationLineItems.
        :type: str
        """

        self._product_description = product_description

    @property
    def product_name(self):
        """
        Gets the product_name of this Riskv1authenticationsOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to `default` or one of the other values that are related to shipping and/or handling. 

        :return: The product_name of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this Riskv1authenticationsOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to `default` or one of the other values that are related to shipping and/or handling. 

        :param product_name: The product_name of this Riskv1authenticationsOrderInformationLineItems.
        :type: str
        """
        if product_name is not None and len(product_name) > 255:
            raise ValueError("Invalid value for `product_name`, length must be less than or equal to `255`")

        self._product_name = product_name

    @property
    def passenger(self):
        """
        Gets the passenger of this Riskv1authenticationsOrderInformationLineItems.

        :return: The passenger of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: Riskv1decisionsOrderInformationPassenger
        """
        return self._passenger

    @passenger.setter
    def passenger(self, passenger):
        """
        Sets the passenger of this Riskv1authenticationsOrderInformationLineItems.

        :param passenger: The passenger of this Riskv1authenticationsOrderInformationLineItems.
        :type: Riskv1decisionsOrderInformationPassenger
        """

        self._passenger = passenger

    @property
    def shipping_destination_types(self):
        """
        Gets the shipping_destination_types of this Riskv1authenticationsOrderInformationLineItems.
        Destination to where the item will be shipped. Example: Commercial, Residential, Store 

        :return: The shipping_destination_types of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: str
        """
        return self._shipping_destination_types

    @shipping_destination_types.setter
    def shipping_destination_types(self, shipping_destination_types):
        """
        Sets the shipping_destination_types of this Riskv1authenticationsOrderInformationLineItems.
        Destination to where the item will be shipped. Example: Commercial, Residential, Store 

        :param shipping_destination_types: The shipping_destination_types of this Riskv1authenticationsOrderInformationLineItems.
        :type: str
        """
        if shipping_destination_types is not None and len(shipping_destination_types) > 50:
            raise ValueError("Invalid value for `shipping_destination_types`, length must be less than or equal to `50`")

        self._shipping_destination_types = shipping_destination_types

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this Riskv1authenticationsOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:   1. You include each line item in your request.  ..- 1st line item has amount=10.00, quantity=1, and taxAmount=0.80  ..- 2nd line item has amount=20.00, quantity=1, and taxAmount=1.60  2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  If you want to include the tax amount and also request the ics_tax service, see Tax Calculation Service Using the SCMP API.  This field is frequently used for Level II and Level III transactions. For details, see `tax_amount` field description in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/) 

        :return: The tax_amount of this Riskv1authenticationsOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this Riskv1authenticationsOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:   1. You include each line item in your request.  ..- 1st line item has amount=10.00, quantity=1, and taxAmount=0.80  ..- 2nd line item has amount=20.00, quantity=1, and taxAmount=1.60  2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  If you want to include the tax amount and also request the ics_tax service, see Tax Calculation Service Using the SCMP API.  This field is frequently used for Level II and Level III transactions. For details, see `tax_amount` field description in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/) 

        :param tax_amount: The tax_amount of this Riskv1authenticationsOrderInformationLineItems.
        :type: str
        """
        if tax_amount is not None and len(tax_amount) > 15:
            raise ValueError("Invalid value for `tax_amount`, length must be less than or equal to `15`")

        self._tax_amount = tax_amount

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
        if not isinstance(other, Riskv1authenticationsOrderInformationLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
