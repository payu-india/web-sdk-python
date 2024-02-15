[**<- back**](/web-sdk-python/README.md)

# settlement_detailsApi
API Command: get_settlement_details

The Settlement Details API is used to retrieve settlement details which the bank has to settle you. The input is the date for which settlement details are required, where the var1 parameter is the date you want to know the settlement status or UTR (Unique Transaction Reference number). For more information, refer to Get Settlement Details API API.

* **Method:**

         POST


*  **Request Header**

        Content-Type  multipart/form-data


* **Request**

  ```class settlementDetailsApis:

    def get_settlement_details(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response
  ```

### Method Arguments


|  Argument   |  Data Type   |                                                                 Description                                                                  |   Value    |
|:-----------:|:------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|:----------:|
|  *var1*   | ```String``` | This parameter must either contain either date for the settlement or UTR (Unique Transaction Reference number). | 8000123    |



