
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
    
1. [Installation](#usage)
2. [Getting Started](#getting-started)
3. [Documentation for various Methods](#documentation-for-various-methods)

## Usage

```shell
pip install payu_websdk
```
## Getting Started

```python
import payu_websdk
client = payu_websdk.Client(<KEY>,<SALT>,<ENV>) # Need to set merchant key,salt and env ("TEST"/"LIVE")
```




## Documentation for various Methods
Method                                                                                                           |  Description
|------------------------------------------------------------------------------------------------------------------| -------------
| [**verifyPayment**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/varify_payment.md)          | Provides the details of a transaction
| [**TransactionDetails**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/Transaction_dtls.md)    | Provides the details of a transactions for a specfic timeperiod
| [**ValidateVPA**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/ValidateUPI.md)               | Used to validate VPA of a user.
| [**RefundTransaction**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/RefunsApi.md)            | Initiate refunds.
| [**DowntimeCheck**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/DowntimeCheck.md)            | Check downtime through bin number.
| [**InvoiceAPI**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/InvoiceAPIs.md)`                 |  Used to create and expire invoice link.
| [**EMI**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/EMIApi.md)                             |  Used for checking the card eligibilty for EMI through the bin number and Check Emi amount according to interest.
| [**CheckIsDomesticapi**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/check_isDomesticapi.md) | The BIN API or check_isDomestic API is used to detect whether a particular BIN number is international or domestic.
| [**CheckoutDetails**](https://github.com/payu-intrepos/web-sdk-java/blob/main/src/CheckoutDetails.md)       |  The get_checkout_details API is a generic API using which they can get information when you create the custom checkout-pages.
