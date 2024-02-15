
[**<- back**](/web-sdk-python/README.md)
# verifyPayment



The Verify Payment (verify_payment) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU’s database after you receive the response.


* **Method:**

         POST


*  **Request Header**

        Content-Type  multipart/form-data


* **Request**

  ```class verifyPayment:

    def verifyPaymentStatusByTransactionID (params):
 
        response = requests.request("POST", url, data=params, headers=headers)
        return response
  ```

### Method Arguments


| Argument | Data Type    | Description   |
|:--------:| :---: | :---: |
| *txnid*  | ```String```   | In this argument you can put all the transaction IDs, that is, txnid (your transaction ID/order ID) values separated by pipe.   |

