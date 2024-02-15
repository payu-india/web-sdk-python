
[**<- back**](https://github.com/payu-india/web-sdk-python?tab=readme-ov-file)
# verifyPayment



The Verify Payment (verify_payment) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU’s database after you receive the response.

* **URL**

         -Test        https://test.payu.in/merchant/postservice.php?form=2

         -Production	https://info.payu.in/merchant/postservice.php?form=2



* **Method:**

         POST


*  **Request Header**

        Content-Type  multipart/form-data


* **Request**

  ```class verifyPayment:

    def verifyPaymentStatusByTransactionID (params):
 
        response = requests.request("POST", url, data=params, headers=headers)
        return response


    def verifyPaymentStatusByPayUID (params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response




  ```



### Method Arguments


| Argument | Data Type    | Description   |
| :---:   | :---: | :---: |
| *txnID*  | ```String```   | In this argument you can put all the transaction IDs, that is, txnid (your transaction ID/order ID) values separated by pipe.   |
