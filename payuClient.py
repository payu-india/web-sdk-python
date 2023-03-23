import os
import json
import pkg_resources

from payu_sdk.base import Base

class payUClient:

    key = ""
    salt = ""
    env = ""

    def __init__(self, credes):
        print (credes)
        print(credes.get("env"))


        self.key = credes.get("key")
        self.salt = credes.get("salt")
        self.env = credes.get("env")
        client = Base()
        client.set_params(credes)
        print(client.env)
        
        




