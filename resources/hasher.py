import hashlib
from payu_sdk.base import Base

key = ""
salt = ""


class Hasher:



    def generate_hash(params):
        base = Base()
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]

        print(key)
        txnid = params.get("txnid")
        print(txnid)
        amount = params.get("amount")
        productinfo = params.get("productinfo")
        firstname = params.get("firstname")
        email = params.get("email", "default")
        udf1 = params.get("udf1", "")
        udf2 = params.get("udf2", "")
        udf3 = params.get("udf3", "")
        udf4 = params.get("udf4", "")
        udf5 = params.get("udf5", "")
        if params.get("additional_charges") is True:
            additional_charges = params.get("additional_charges")
            payment_hash_sequence = f"{additional_charges}|{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"

        else:
            payment_hash_sequence = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"

        hash_value = hashlib.sha512((payment_hash_sequence).encode('utf-8')).hexdigest()

        return hash_value

    def validate_hash(params):
        base = Base()
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]
        txnid = params.get("txnid")
        amount = params.get("amount")
        productinfo = params.get("productinfo")
        firstname = params.get("firstname")
        email = params.get("email", "default")
        udf1 = params.get("udf1", "")
        udf2 = params.get("udf2", "")
        udf3 = params.get("udf3", "")
        udf4 = params.get("udf4", "")
        udf5 = params.get("udf5", "")

        if params.get("additional_charges") is True:
            additional_charges = params.get("additional_charges")
            validate_hash_sequence = f"{additional_charges}|{salt}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"
        else:
            validate_hash_sequence = f"{salt}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"

        validate_hash = hashlib.sha512((validate_hash_sequence).encode('utf-8')).hexdigest().lower()
        return validate_hash



    def APIHash(params):

        base = Base()
        client_creds = base.get_params()
        key = client_creds[0]
        salt = client_creds[1]

        command = params.get("command")
        var1 = params.get("var1")

        hash_sequence = f"{key}|{command}|{var1}|{salt}"

        hash_value = hashlib.sha512((hash_sequence).encode('utf-8')).hexdigest().lower()
        return hash_value

