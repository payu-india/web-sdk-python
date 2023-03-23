



import hashlib
from payu_sdk.base import Base
import requests

key = ""
salt = ""

url = "https://test.payu.in/merchant/postservice?form=2"
headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

class verifyPayment:

    def verifyPaymentStatusByTransactionID (params):
 
        response = requests.request("POST", url, data=params, headers=headers)
        return response


    def verifyPaymentStatusByPayUID (params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response



''' 
 This API is used to check the status of refund/cancel requests. 
 Whenever the cancel_refund_transaction API is executed successfully, a request ID is returned in the output parameters for that particular request, 
 var1 is Request ID which is returned in the output parameters for that particular request. 
 
 '''
class RefundAPI:

    def refundTransaction (params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response




class BinAPI:

    def fetchCardDetailsByBIN (params):
        base = Base()
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]

        response = requests.request("POST", url, data=params, headers=headers)
        return response




class EmiAPIs:

    def eligibleBinsForEMI(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response



    def getEmiAmountAccordingToInterest(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response



class GetCheckoutDetailsApi:

    def get_checkout_details(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response



class settlementDetailsApis:

    def get_settlement_details(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response



class DowntimeCheckAPIs:

    def getNetbankingStatus(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response


    def getIssuingBankStatus(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response



class InvoiceAPIs:

    def create_invoice(params):

        response = requests.request("POST", url, data=params, headers=headers)
        return response














