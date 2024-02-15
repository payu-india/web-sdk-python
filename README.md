
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
| [**verifyPayment**](/web-sdk-python/docs/verifyPayment.md)            | Provides the details of a transaction
| [**RefundTransaction**](/web-sdk-python/docs/RefundAPI.md)            | Initiate refunds.
| [**BinAPI**](/web-sdk-python/docs)            | check the bin info.
| [**EligibleBinsForEMI**](/web-sdk-python/docs/eligibleBinsForEMI.md)            | Used for checking the card eligibilty for EMI through the bin number..
| [**EmiAmountAccordingToInterest**](/web-sdk-python/docs/getEmiAmountAccordingToInterest.md)            | Used to fetch interest accordign to Banks and tenure..
| [**settlementAPI**](/web-sdk-python/docs/settlementDetailsApis.md)            | Used to fetch settlement details for a particular date..
| [**getNetbankingStatus**](/web-sdk-python/docs/getNetbankingStatus.md)            | Check downtime status of PGs..
| [**getIssuingBankStatus**](/web-sdk-python/docs/getIssuingBankStatus.md)            | Check downtime through bin number..
| [**InvoiceAPIs**](/web-sdk-python/docs/InvoiceAPIs.md)            | Used to create email and SMS invoice ( Pay by link ).
