[**<- back**](/web-sdk-python/README.md)

# getIssuingBankStatus

This API is used to help you in handling the credit card/debit card issuing bank’s downtime. It allows you to get the present status of the issuing bank using the specific Bank Identification Number (BIN). BIN is identified as the first six digits of a credit or debit card. You need to provide the BIN number as input and the corresponding issuing bank’s status would be returned in the output (whether up or down).
This API is used to retrieve the card BINs for all banks which are observing either full downtime or partial downtime at an instant. The information related to full/partial downtime depends on the input.
This section describes how to use the following APIs:

* **Method:**

         POST


*  **Request Header**

        Content-Type  multipart/form-data

* **Request**

  ```class DowntimeCheckAPIs:


    def getIssuingBankStatus(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response
  ```



### Method Arguments


| Argument | Data Type  | Description| Example |
|:--------:|:----------:|:--------------------------------------------------:|:-------:|
|  *bin*   | ```Integer``` |This parameter must contain the bank identification number | 123456  |
