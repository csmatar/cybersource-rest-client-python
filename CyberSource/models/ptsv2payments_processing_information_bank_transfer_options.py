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


class Ptsv2paymentsProcessingInformationBankTransferOptions(object):
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
        'decline_avs_flags': 'str',
        'sec_code': 'str',
        'terminal_city': 'str',
        'terminal_state': 'str',
        'effective_date': 'str',
        'partial_payment_id': 'str',
        'customer_memo': 'str',
        'payment_category_code': 'str',
        'settlement_method': 'str',
        'fraud_screening_level': 'str'
    }

    attribute_map = {
        'decline_avs_flags': 'declineAvsFlags',
        'sec_code': 'secCode',
        'terminal_city': 'terminalCity',
        'terminal_state': 'terminalState',
        'effective_date': 'effectiveDate',
        'partial_payment_id': 'partialPaymentId',
        'customer_memo': 'customerMemo',
        'payment_category_code': 'paymentCategoryCode',
        'settlement_method': 'settlementMethod',
        'fraud_screening_level': 'fraudScreeningLevel'
    }

    def __init__(self, decline_avs_flags=None, sec_code=None, terminal_city=None, terminal_state=None, effective_date=None, partial_payment_id=None, customer_memo=None, payment_category_code=None, settlement_method=None, fraud_screening_level=None):
        """
        Ptsv2paymentsProcessingInformationBankTransferOptions - a model defined in Swagger
        """

        self._decline_avs_flags = None
        self._sec_code = None
        self._terminal_city = None
        self._terminal_state = None
        self._effective_date = None
        self._partial_payment_id = None
        self._customer_memo = None
        self._payment_category_code = None
        self._settlement_method = None
        self._fraud_screening_level = None

        if decline_avs_flags is not None:
          self.decline_avs_flags = decline_avs_flags
        if sec_code is not None:
          self.sec_code = sec_code
        if terminal_city is not None:
          self.terminal_city = terminal_city
        if terminal_state is not None:
          self.terminal_state = terminal_state
        if effective_date is not None:
          self.effective_date = effective_date
        if partial_payment_id is not None:
          self.partial_payment_id = partial_payment_id
        if customer_memo is not None:
          self.customer_memo = customer_memo
        if payment_category_code is not None:
          self.payment_category_code = payment_category_code
        if settlement_method is not None:
          self.settlement_method = settlement_method
        if fraud_screening_level is not None:
          self.fraud_screening_level = fraud_screening_level

    @property
    def decline_avs_flags(self):
        """
        Gets the decline_avs_flags of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Space-separated list of AVS flags that cause the request to be declined for AVS reasons.  **Important** To receive declines for the AVS code `N`, you must include the value `N` in the space-separated list.  ### AVS Codes for Cielo 3.0 and CyberSource Latin American Processing  **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this section is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  |AVS Code|Description| |--- |--- | |D|Partial match: postal code and address match.| |E|Not supported: AVS is not supported for this card type. _or_ Invalid: the acquirer returned an unrecognized value for the AVS response.| |F|Partial match: postal code matches, but CPF and address do not match.*| |G|Not supported: AVS not supported or not verified.| |I|No match: AVS information is not available.| |K|Partial match: CPF matches, but postal code and address do not match.*| |L|Partial match: postal code and CPF match, but address does not match.*| |N|No match: postal code, CPF, and address do not match.*| |O|Partial match: CPF and address match, but postal code does not match.*| |R|Not supported: your implementation does not support AVS _or_ System unavailable.| |T|Partial match: address matches, but postal code and CPF do not match.*| |V|Match: postal code, CPF, and address match.*| |* CPF (Cadastro de Pessoas Fisicas) is required only for Redecard in Brazil.||  ### AVS Codes for All Other Processors  **Note** The list of AVS codes for all other processors follows these descriptions of the processor-specific information for these codes.  #### American Express Cards For American Express cards only, you can receive Visa and CyberSource AVS codes in addition to the American Express AVS codes.  **Note** For Visa Platform Connect, the American Express AVS codes are converted to Visa AVS codes before they are returned to you. As a result, you will not receive American Express AVS codes for the American Express card type.  _American Express Card codes_: `F`, `H`, `K`, `L`, `O`, `T`, `V`  #### Domestic and International Visa Cards The international and domestic alphabetic AVS codes are the Visa standard AVS codes. CyberSource maps the standard AVS return codes for other types of payment cards, including American Express cards, to the Visa standard AVS codes.  AVS is considered either domestic or international, depending on the location of the bank that issued the customer’s payment card: - When the bank is in the U.S., the AVS is domestic. - When the bank is outside the U.S., the AVS is international.  You should be prepared to handle both domestic and international AVS result codes: - For international cards, you can receive domestic AVS codes in addition to the international AVS codes. - For domestic cards, you can receive international AVS codes in addition to the domestic AVS codes.  _International Visa Codes_: `B`, `C`, `D`, `G`, `I`, `M`, `P`  _Domestic Visa Codes_: `A`, `E`,`N`, `R`, `S`, `U`, `W`, `X`, `Y`, `Z`  #### CyberSource Codes The numeric AVS codes are created by CyberSource and are not standard Visa codes. These AVS codes can be returned for any card type.  _CyberSource Codes_: `1`, `2`, `3`, `4`  ### Table of AVS Codes for All Other Processors  |AVS Code|Description| |--- |--- | |A|Partial match: street address matches, but 5-digit and 9-digit postal codes do not match.| |B|Partial match: street address matches, but postal code is not verified. Returned only for Visa cards not issued in the U.S.| |C|No match: street address and postal code do not match. Returned only for Visa cards not issued in the U.S.| |D & M|Match: street address and postal code match. Returned only for Visa cards not issued in the U.S.| |E|Invalid: AVS data is invalid or AVS is not allowed for this card type.| |F|Partial match: card member’s name does not match, but billing postal code matches.| |G|Not supported: issuing bank outside the U.S. does not support AVS.| |H|Partial match: card member’s name does not match, but street address and postal code match. Returned only for the American Express card type.| |I|No match: address not verified. Returned only for Visa cards not issued in the U.S.| |K|Partial match: card member’s name matches, but billing address and billing postal code do not match. Returned only for the American Express card type.| |L|Partial match: card member’s name and billing postal code match, but billing address does not match. Returned only for the American Express card type.| |M|See the entry for D & M.| |N|No match: one of the following: street address and postal code do not match _or_ (American Express card type only) card member’s name, street address, and postal code do not match.| |O|Partial match: card member’s name and billing address match, but billing postal code does not match. Returned only for the American Express card type.| |P|Partial match: postal code matches, but street address not verified. Returned only for Visa cards not issued in the U.S.| |R|System unavailable.| |S|Not supported: issuing bank in the U.S. does not support AVS.| |T|Partial match: card member’s name does not match, but street address matches. Returned only for the American Express card type.| |U|System unavailable: address information unavailable for one of these reasons: The U.S. bank does not support AVS outside the U.S. _or_ The AVS in a U.S. bank is not functioning properly.| |V|Match: card member’s name, billing address, and billing postal code match. Returned only for the American Express card type.| |W|Partial match: street address does not match, but 9-digit postal code matches.| |X|Match: street address and 9-digit postal code match.| |Y|Match: street address and 5-digit postal code match.| |Z|Partial match: street address does not match, but 5-digit postal code matches.| |1|Not supported: one of the following: AVS is not supported for this processor or card type _or_ AVS is disabled for your CyberSource account. To enable AVS, contact CyberSource Customer Support.| |2|Unrecognized: the processor returned an unrecognized value for the AVS response.| |3|Match: address is confirmed. Returned only for PayPal Express Checkout.| |4|No match: address is not confirmed. Returned only for PayPal Express Checkout.| |5|No match: no AVS code was returned by the processor.| 

        :return: The decline_avs_flags of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._decline_avs_flags

    @decline_avs_flags.setter
    def decline_avs_flags(self, decline_avs_flags):
        """
        Sets the decline_avs_flags of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Space-separated list of AVS flags that cause the request to be declined for AVS reasons.  **Important** To receive declines for the AVS code `N`, you must include the value `N` in the space-separated list.  ### AVS Codes for Cielo 3.0 and CyberSource Latin American Processing  **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this section is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  |AVS Code|Description| |--- |--- | |D|Partial match: postal code and address match.| |E|Not supported: AVS is not supported for this card type. _or_ Invalid: the acquirer returned an unrecognized value for the AVS response.| |F|Partial match: postal code matches, but CPF and address do not match.*| |G|Not supported: AVS not supported or not verified.| |I|No match: AVS information is not available.| |K|Partial match: CPF matches, but postal code and address do not match.*| |L|Partial match: postal code and CPF match, but address does not match.*| |N|No match: postal code, CPF, and address do not match.*| |O|Partial match: CPF and address match, but postal code does not match.*| |R|Not supported: your implementation does not support AVS _or_ System unavailable.| |T|Partial match: address matches, but postal code and CPF do not match.*| |V|Match: postal code, CPF, and address match.*| |* CPF (Cadastro de Pessoas Fisicas) is required only for Redecard in Brazil.||  ### AVS Codes for All Other Processors  **Note** The list of AVS codes for all other processors follows these descriptions of the processor-specific information for these codes.  #### American Express Cards For American Express cards only, you can receive Visa and CyberSource AVS codes in addition to the American Express AVS codes.  **Note** For Visa Platform Connect, the American Express AVS codes are converted to Visa AVS codes before they are returned to you. As a result, you will not receive American Express AVS codes for the American Express card type.  _American Express Card codes_: `F`, `H`, `K`, `L`, `O`, `T`, `V`  #### Domestic and International Visa Cards The international and domestic alphabetic AVS codes are the Visa standard AVS codes. CyberSource maps the standard AVS return codes for other types of payment cards, including American Express cards, to the Visa standard AVS codes.  AVS is considered either domestic or international, depending on the location of the bank that issued the customer’s payment card: - When the bank is in the U.S., the AVS is domestic. - When the bank is outside the U.S., the AVS is international.  You should be prepared to handle both domestic and international AVS result codes: - For international cards, you can receive domestic AVS codes in addition to the international AVS codes. - For domestic cards, you can receive international AVS codes in addition to the domestic AVS codes.  _International Visa Codes_: `B`, `C`, `D`, `G`, `I`, `M`, `P`  _Domestic Visa Codes_: `A`, `E`,`N`, `R`, `S`, `U`, `W`, `X`, `Y`, `Z`  #### CyberSource Codes The numeric AVS codes are created by CyberSource and are not standard Visa codes. These AVS codes can be returned for any card type.  _CyberSource Codes_: `1`, `2`, `3`, `4`  ### Table of AVS Codes for All Other Processors  |AVS Code|Description| |--- |--- | |A|Partial match: street address matches, but 5-digit and 9-digit postal codes do not match.| |B|Partial match: street address matches, but postal code is not verified. Returned only for Visa cards not issued in the U.S.| |C|No match: street address and postal code do not match. Returned only for Visa cards not issued in the U.S.| |D & M|Match: street address and postal code match. Returned only for Visa cards not issued in the U.S.| |E|Invalid: AVS data is invalid or AVS is not allowed for this card type.| |F|Partial match: card member’s name does not match, but billing postal code matches.| |G|Not supported: issuing bank outside the U.S. does not support AVS.| |H|Partial match: card member’s name does not match, but street address and postal code match. Returned only for the American Express card type.| |I|No match: address not verified. Returned only for Visa cards not issued in the U.S.| |K|Partial match: card member’s name matches, but billing address and billing postal code do not match. Returned only for the American Express card type.| |L|Partial match: card member’s name and billing postal code match, but billing address does not match. Returned only for the American Express card type.| |M|See the entry for D & M.| |N|No match: one of the following: street address and postal code do not match _or_ (American Express card type only) card member’s name, street address, and postal code do not match.| |O|Partial match: card member’s name and billing address match, but billing postal code does not match. Returned only for the American Express card type.| |P|Partial match: postal code matches, but street address not verified. Returned only for Visa cards not issued in the U.S.| |R|System unavailable.| |S|Not supported: issuing bank in the U.S. does not support AVS.| |T|Partial match: card member’s name does not match, but street address matches. Returned only for the American Express card type.| |U|System unavailable: address information unavailable for one of these reasons: The U.S. bank does not support AVS outside the U.S. _or_ The AVS in a U.S. bank is not functioning properly.| |V|Match: card member’s name, billing address, and billing postal code match. Returned only for the American Express card type.| |W|Partial match: street address does not match, but 9-digit postal code matches.| |X|Match: street address and 9-digit postal code match.| |Y|Match: street address and 5-digit postal code match.| |Z|Partial match: street address does not match, but 5-digit postal code matches.| |1|Not supported: one of the following: AVS is not supported for this processor or card type _or_ AVS is disabled for your CyberSource account. To enable AVS, contact CyberSource Customer Support.| |2|Unrecognized: the processor returned an unrecognized value for the AVS response.| |3|Match: address is confirmed. Returned only for PayPal Express Checkout.| |4|No match: address is not confirmed. Returned only for PayPal Express Checkout.| |5|No match: no AVS code was returned by the processor.| 

        :param decline_avs_flags: The decline_avs_flags of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if decline_avs_flags is not None and len(decline_avs_flags) > 15:
            raise ValueError("Invalid value for `decline_avs_flags`, length must be less than or equal to `15`")

        self._decline_avs_flags = decline_avs_flags

    @property
    def sec_code(self):
        """
        Gets the sec_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Specifies the authorization method for the transaction.  #### TeleCheck Accepts only the following values: - `ARC`: account receivable conversion - `CCD`: corporate cash disbursement - `POP`: point of purchase conversion - `PPD`: prearranged payment and deposit entry - `TEL`: telephone-initiated entry - `WEB`: internet-initiated entry  For details, see `ecp_sec_code` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The sec_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._sec_code

    @sec_code.setter
    def sec_code(self, sec_code):
        """
        Sets the sec_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Specifies the authorization method for the transaction.  #### TeleCheck Accepts only the following values: - `ARC`: account receivable conversion - `CCD`: corporate cash disbursement - `POP`: point of purchase conversion - `PPD`: prearranged payment and deposit entry - `TEL`: telephone-initiated entry - `WEB`: internet-initiated entry  For details, see `ecp_sec_code` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param sec_code: The sec_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if sec_code is not None and len(sec_code) > 3:
            raise ValueError("Invalid value for `sec_code`, length must be less than or equal to `3`")

        self._sec_code = sec_code

    @property
    def terminal_city(self):
        """
        Gets the terminal_city of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        City in which the terminal is located. If more than four alphanumeric characters are submitted, the transaction will be declined.  You cannot include any special characters. 

        :return: The terminal_city of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._terminal_city

    @terminal_city.setter
    def terminal_city(self, terminal_city):
        """
        Sets the terminal_city of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        City in which the terminal is located. If more than four alphanumeric characters are submitted, the transaction will be declined.  You cannot include any special characters. 

        :param terminal_city: The terminal_city of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if terminal_city is not None and len(terminal_city) > 4:
            raise ValueError("Invalid value for `terminal_city`, length must be less than or equal to `4`")

        self._terminal_city = terminal_city

    @property
    def terminal_state(self):
        """
        Gets the terminal_state of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        State in which the terminal is located. If more than two alphanumeric characters are submitted, the transaction will be declined.  You cannot include any special characters. 

        :return: The terminal_state of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._terminal_state

    @terminal_state.setter
    def terminal_state(self, terminal_state):
        """
        Sets the terminal_state of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        State in which the terminal is located. If more than two alphanumeric characters are submitted, the transaction will be declined.  You cannot include any special characters. 

        :param terminal_state: The terminal_state of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if terminal_state is not None and len(terminal_state) > 2:
            raise ValueError("Invalid value for `terminal_state`, length must be less than or equal to `2`")

        self._terminal_state = terminal_state

    @property
    def effective_date(self):
        """
        Gets the effective_date of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Effective date for the transaction. The effective date must be within 45 days of the current day. If you do not include this value, CyberSource sets the effective date to the next business day.  Format: `MMDDYYYY`  Supported only for the CyberSource ACH Service. 

        :return: The effective_date of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """
        Sets the effective_date of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Effective date for the transaction. The effective date must be within 45 days of the current day. If you do not include this value, CyberSource sets the effective date to the next business day.  Format: `MMDDYYYY`  Supported only for the CyberSource ACH Service. 

        :param effective_date: The effective_date of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if effective_date is not None and len(effective_date) > 8:
            raise ValueError("Invalid value for `effective_date`, length must be less than or equal to `8`")

        self._effective_date = effective_date

    @property
    def partial_payment_id(self):
        """
        Gets the partial_payment_id of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Identifier for a partial payment or partial credit.  The value for each debit request or credit request must be unique within the scope of the order. For details, see `partial_payment_id` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The partial_payment_id of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._partial_payment_id

    @partial_payment_id.setter
    def partial_payment_id(self, partial_payment_id):
        """
        Sets the partial_payment_id of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Identifier for a partial payment or partial credit.  The value for each debit request or credit request must be unique within the scope of the order. For details, see `partial_payment_id` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param partial_payment_id: The partial_payment_id of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if partial_payment_id is not None and len(partial_payment_id) > 25:
            raise ValueError("Invalid value for `partial_payment_id`, length must be less than or equal to `25`")

        self._partial_payment_id = partial_payment_id

    @property
    def customer_memo(self):
        """
        Gets the customer_memo of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Payment related information.  This information is included on the customer’s statement. 

        :return: The customer_memo of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._customer_memo

    @customer_memo.setter
    def customer_memo(self, customer_memo):
        """
        Sets the customer_memo of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Payment related information.  This information is included on the customer’s statement. 

        :param customer_memo: The customer_memo of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if customer_memo is not None and len(customer_memo) > 80:
            raise ValueError("Invalid value for `customer_memo`, length must be less than or equal to `80`")

        self._customer_memo = customer_memo

    @property
    def payment_category_code(self):
        """
        Gets the payment_category_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Flag that indicates whether to process the payment.  Use with deferred payments. For details, see `ecp_payment_mode` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  Possible values: - `0`: Standard debit with immediate payment (default). - `1`: For deferred payments, indicates that this is a deferred payment and that you will send a debit request with `paymentCategoryCode = 2` in the future. - `2`: For deferred payments, indicates notification to initiate payment.  #### Chase Paymentech Solutions and TeleCheck Use for deferred and partial payments.  #### CyberSource ACH Service Not used.  #### RBS WorldPay Atlanta Not used. 

        :return: The payment_category_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._payment_category_code

    @payment_category_code.setter
    def payment_category_code(self, payment_category_code):
        """
        Sets the payment_category_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Flag that indicates whether to process the payment.  Use with deferred payments. For details, see `ecp_payment_mode` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  Possible values: - `0`: Standard debit with immediate payment (default). - `1`: For deferred payments, indicates that this is a deferred payment and that you will send a debit request with `paymentCategoryCode = 2` in the future. - `2`: For deferred payments, indicates notification to initiate payment.  #### Chase Paymentech Solutions and TeleCheck Use for deferred and partial payments.  #### CyberSource ACH Service Not used.  #### RBS WorldPay Atlanta Not used. 

        :param payment_category_code: The payment_category_code of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if payment_category_code is not None and len(payment_category_code) > 1:
            raise ValueError("Invalid value for `payment_category_code`, length must be less than or equal to `1`")

        self._payment_category_code = payment_category_code

    @property
    def settlement_method(self):
        """
        Gets the settlement_method of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Method used for settlement.  Possible values: - `A`: Automated Clearing House (default for credits and for transactions using Canadian dollars) - `F`: Facsimile draft (U.S. dollars only) - `B`: Best possible (U.S. dollars only) (default if the field has not already been configured for your merchant ID)  For details, see `ecp_settlement_method` field description for credit cars and `ecp_debit_settlement_method` for debit cards in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The settlement_method of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._settlement_method

    @settlement_method.setter
    def settlement_method(self, settlement_method):
        """
        Sets the settlement_method of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Method used for settlement.  Possible values: - `A`: Automated Clearing House (default for credits and for transactions using Canadian dollars) - `F`: Facsimile draft (U.S. dollars only) - `B`: Best possible (U.S. dollars only) (default if the field has not already been configured for your merchant ID)  For details, see `ecp_settlement_method` field description for credit cars and `ecp_debit_settlement_method` for debit cards in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param settlement_method: The settlement_method of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if settlement_method is not None and len(settlement_method) > 1:
            raise ValueError("Invalid value for `settlement_method`, length must be less than or equal to `1`")

        self._settlement_method = settlement_method

    @property
    def fraud_screening_level(self):
        """
        Gets the fraud_screening_level of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Level of fraud screening.  Possible values: - `1`: Validation — default if the field has not already been configured for your merchant ID - `2`: Verification  For a description of this feature and a list of supported processors, see \"Verification and Validation\" in the [Electronic Check Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm). 

        :return: The fraud_screening_level of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._fraud_screening_level

    @fraud_screening_level.setter
    def fraud_screening_level(self, fraud_screening_level):
        """
        Sets the fraud_screening_level of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        Level of fraud screening.  Possible values: - `1`: Validation — default if the field has not already been configured for your merchant ID - `2`: Verification  For a description of this feature and a list of supported processors, see \"Verification and Validation\" in the [Electronic Check Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm). 

        :param fraud_screening_level: The fraud_screening_level of this Ptsv2paymentsProcessingInformationBankTransferOptions.
        :type: str
        """
        if fraud_screening_level is not None and len(fraud_screening_level) > 1:
            raise ValueError("Invalid value for `fraud_screening_level`, length must be less than or equal to `1`")

        self._fraud_screening_level = fraud_screening_level

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
        if not isinstance(other, Ptsv2paymentsProcessingInformationBankTransferOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
