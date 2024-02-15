[**<- back**](/web-sdk-python/README.md)

# getNetbankingStatus
The Downtime Check APIs help you get  the downtime of the Net Banking or card BINs for all the banks which are observing either full downtime or partial downtime.


* **Method:**

         POST


*  **Request Header**

        Content-Type  multipart/form-data

* **Request**

  ```class DowntimeCheckAPIs:

    def getNetbankingStatus(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response
  ```


### Method Arguments

|  Argument  | Data Type | Description |    Example     |
|:----------:|:---------:|:--------------------------------------------------:|:--------------:|
| *bankCode* | ```String``` |This parameter must contain any of NetBanking code or default | AXIB/“default” |
