[**<- back**](/web-sdk-python/README.md)

# cancelRefundTransaction
API Command: cancel_refund_transaction

The Cancel Refund Transaction API (cancel_refund_transaction) can be used for the following purposes:

Cancel a transaction that is in ‘auth’ state at the moment
Refund a transaction that is in a ‘captured’ state at the moment.
In this API: var1 is the Payu ID (mihpayid) of the transaction, var2 should contain the Token ID (unique token from the merchant), and va

* **Method:**

         POST


*  **Request Header**

        Content-Type  multipart/form-data


* **Request**

  ```class RefundAPI:

    def refundTransaction (params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response
  ```

### Method Arguments


|  Argument   |  Data Type   |                                                                 Description                                                                  |   Value    |
|:-----------:|:------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|:----------:|
|  *payuid*   | ```String``` | This parameter must contain the Payu ID (mihpayid) of the transaction. For more information on mihpayid, refer to the Post Parameters table. | 8000123    |
| *requestId* | ```String``` |                              This parameter must contain the request ID (unique request Id to track the refund)                              |  20221027  |
|  *amount*   | ```Number``` | For captured transaction:This parameter must contain the amount which needs to be refunded. Both partial and full refunds are allowed.      |    500     |


