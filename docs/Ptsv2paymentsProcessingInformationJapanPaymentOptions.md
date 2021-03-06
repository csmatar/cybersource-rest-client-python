# Ptsv2paymentsProcessingInformationJapanPaymentOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | This value is a 2-digit code indicating the payment method. Use Payment Method Code value that applies to the tranasction. - 10 (One-time payment) - 21, 22, 23, 24  (Bonus(one-time)payment) - 61 (Installment payment) - 31, 32, 33, 34  (Integrated (Bonus + Installment)payment) - 80 (Revolving payment)  | [optional] 
**installments** | **str** | Number of Installments.  | [optional] 
**terminal_id** | **str** | Unique Japan Credit Card Association (JCCA) terminal identifier.  The difference between this field and the &#x60;pointOfSaleInformation.terminalID&#x60; field is that you can define &#x60;pointOfSaleInformation.terminalID&#x60;, but &#x60;processingInformation.japanPaymentOptions.terminalId&#x60; is defined by the JCCA and is used only in Japan.  This field is supported only on CyberSource through VisaNet and JCN Gateway.  Optional field.  | [optional] 
**first_billing_month** | **str** | Billing month in MM format.  | [optional] 
**business_name** | **str** | Business name in Japanese characters. This field is supported only on JCN Gateway and for the Sumitomo Mitsui Card Co. acquirer on CyberSource through VisaNet.  | [optional] 
**business_name_katakana** | **str** | Business name in Katakana characters. This field is supported only on JCN Gateway and for the Sumitomo Mitsui Card Co. acquirer on CyberSource through VisaNet.  | [optional] 
**jis2_track_data** | **str** | Japanese Industrial Standard Type 2 (JIS2) track data from the front of the card.  This field is supported only on CyberSource through VisaNet and JCN Gateway.  Optional field.  | [optional] 
**business_name_alpha_numeric** | **str** | Business name in alphanumeric characters. This field is supported only on JCN Gateway and for the Sumitomo Mitsui Card Co. acquirer on CyberSource through VisaNet.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


