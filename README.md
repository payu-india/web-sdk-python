
# PayU SDK for Python Apis
This API gives you the status of the transaction. PayU recommends this API to reconcile with PayU’s database after you receive the response, where var1 is your transaction id.

## Features Supported
Following features are supported in the PayU Python web SDK:
- Create Payment Link.
- Verify transactions, check the transaction status, transaction details, or discount rate for a transaction
- Initiated refunds, cancel refund, check refund status.
- Retrieve settlement details which the bank has to settle you.
- Get information of the payment options, offers, recommendations, and downtime details.
- Check the customer’s eligibility for EMI and get the EMI amount according to interest
- Pay by link
  To get started with PayU, visit our [Developer Guide](https://devguide.payu.in/low-code-web-sdk/getting-started-low-code-web-sdk/register-for-a-test-merchant-account/)
# Table of Contents
    
1. [Usage](#usage)
2. [Getting Started](#getting-started)
3. [Documentation for various Methods](#documentation-for-various-methods)
## Usage
import (
Payu "https://github.com/payu-india/web-sdk-python"
)

## Getting Started


```shell
key =""
salt =""
client = payu_sdk.payUClient({"key":key,"salt":salt,"env":env})
// Need to set merchant key and salt
  
```




## Documentation for various Methods
Method                                                                                                           |  Description
|------------------------------------------------------------------------------------------------------------------| -------------
| [**Verify_payment**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/varify_payment.md) ```[async]```          | Provides the details of a transaction
| [**TransactionDetails**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/Transaction_dtls.md) ```[async]```    | Provides the details of a transactions for a specfic timeperiod
| [**ValidateVPA**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/ValidateUPI.md) ```[async]```                | Used to validate VPA of a user.
| [**RefundTransaction**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/RefunsApi.md) ```[async]```            | Initiate refunds.
| [**DowntimeCheck**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/DowntimeCheck.md) ```[async]```            | Check downtime through bin number.
| [**InvoiceAPI**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/InvoiceAPIs.md) ```[async]```                 |  Used to create and expire invoice link.
| [**EMI**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/EMIApi.md) ```[async]```                             |  Used for checking the card eligibilty for EMI through the bin number and Check Emi amount according to interest.
| [**Check_isDomesticapi**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/check_isDomesticapi.md)```[async]``` | The BIN API or check_isDomestic API is used to detect whether a particular BIN number is international or domestic.
| [**CheckoutDetails**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/CheckoutDetails.md) ```[async]```        |  The get_checkout_details API is a generic API using which they can get information when you create the custom checkout-pages.
