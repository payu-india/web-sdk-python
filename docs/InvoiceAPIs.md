[**<- back**](/README.md)

# createInvoice
Create an email professional invoices so that your customers, wherever they are, can pay you faster. Use the PayU Invoicing solution to send or manage invoices.

PayU helps you send Invoices to your customers through email using the following APIs:

* **Method:**

         POST


*  **Request Header**

        Content-Type  multipart/form-data


* **Request**

  ```class InvoiceAPIs:

    def create_invoice(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response
  ```



### Method Arguments

* create_invoice

| Argument  |                                               Description                                               |                                                                                                                                                Value                                                                                                                                                |
|:---------:|:-------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| *payload* |   The payload parameter must be generated in the HashMap mentioned in the sample value string above.    | {“amount“:”10000”,”txnid“:”abaac3332″,”productinfo“:”iPhone”,”firstname“:”Samir”,”em ail“:”test@test.com”,”phone“:”9988776655”,”address1“:”testaddress”,”city“:”Mumbai”,”stat e“:”Maharashtra”,”country“:”India”,”zipcode“:”122002″,”template_id“:”14″,”validation_period“: 6,”send_email_now“:”1”} |
