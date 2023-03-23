


import hashlib
from payu_sdk.base import Base
import requests

key = ""
salt = ""
env = ""


url = "https://test.payu.in/_payment"
headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}



class createRequest:


    
    def paymentRequest(payload):
        base = Base()
        client_creds = base.get_params()
        print(client_creds)
        key = client_creds[0]
        salt = client_creds[1]
        env = client_creds[2]

        print(env)

       

        print(( "<form name=\"payment_post\" id=\"payment_post\" action=\"https://test.payu.in/_payment\" method=\"post\">"))
        print("<input hidden type='text' name='key'' value='" + key + "'/>")
        for parameter, value in payload.items():
            print("<input hidden type='text' name='" + parameter + "' value='" + value + "'/>")
          
        print(("</form><script type='text/javascript'>\n" +
            "                            window.onload=function(){\n" +
            "                                document.forms['payment_post'].submit();\n" +
            "                            }\n" +
            "                        </script>"))
        

        response = requests.request("POST", url, data=payload, headers=headers)
        return response

        

         
        









