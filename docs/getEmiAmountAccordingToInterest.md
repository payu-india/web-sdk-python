
[**<- back**](/web-sdk-python/README.md)

# getEmiAmountAccordingToInterest
The EMI APIs allows you to fetch the EMI amount according to interest.

* **Method:**

         POST

*  **Request Header**

        Content-Type  multipart/form-data

* **Request**

  ```class EmiAPIs:

    def getEmiAmountAccordingToInterest(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response

  ```


### Method Arguments


| Argument |  Data Type   |                              Description             |                   Example           |
|:--------:|:------------:|:-----------------------------------------:|:---------------------------------------:|
| *amount* | ```Number``` | The amount that must be converted to EMI. |                  10000                  |
