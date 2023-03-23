import unittest
import payu_sdk

'# Please Note below:'
'# 1). key (i.e. gtKFFx) is testing key, you need to put your own production key before going live'
'# 2). udf1 to udf5 are optional values (i.e. you pass user defined values to these fields e.g. street name, city, address etc.'
'# 3). You should always validate hash after transaction response at your success-failure urls'
'# 4). For more info, please follow document from here : https://github.com/payu-intrepos/Documentations/wiki/Server-Side '



parameters = {"key": "gtKFFx", "txnid": "20200429103010", "productinfo": "iPhone", "firstname": "Ashish",
                      "email": "test@gmail.com", "amount": "10","udf1":"","udf2":"","udf3":"","udf4":"","udf5":""}
payment_hash = "672de0802e96766044e473db706bdb1f14dea0ad3b3a69fed02377233a8bb73c646a43520bf0d7217647945ac0f0602c49e3b4109c379df75d8dbb1d4702ae6b"
reverse_hash = "57230620dcf90ed58c96b57c508d89431788cc7ab6b7d472aeb1e014ea7fa712cdc00f986bf3e6df8f5c6ebce70340286d57623590a3c8e4ced3b551e792b3d3"
class TestPayUHashes(unittest.TestCase):


    def test_generate_hash(self):

        result = payu_sdk.Hasher.generate_hash(parameters)
        self.assertEqual(result, payment_hash)
        self.assertEqual(len(parameters['key']), 6)
        self.assertIsNot(parameters['key'], "", "key should not be empty")
        self.assertIsNot(parameters['txnid'], "", "txnid should not be empty")
        self.assertIsNot(parameters['amount'], "", "amount should not be empty")
        self.assertIsNot(parameters['productinfo'], "", "productinfo should not be empty")
        self.assertLess(len(parameters['txnid']), 35, "Length of txnid is allowed to 35")
        self.assertLess(len(parameters['udf1']), 65, "Length of udf1 is allowed to 65")
        self.assertLess(len(parameters['udf2']), 65, "Length of udf2 is allowed to 65")
        self.assertLess(len(parameters['udf3']), 65, "Length of udf3 is allowed to 65")
        self.assertLess(len(parameters['udf4']), 65, "Length of udf4 is allowed to 65")
        self.assertLess(len(parameters['udf5']), 65, "Length of udf5 is allowed to 65")




    def test_validate_hash(self):
        result = payu_sdk.Hasher.validate_hash(parameters)
        self.assertEqual(result, reverse_hash)
        self.assertEqual(len(parameters['key']), 6)
        self.assertIsNot(parameters['key'], "", "key should not be empty")
        self.assertIsNot(parameters['txnid'], "", "txnid should not be empty")
        self.assertIsNot(parameters['amount'], "", "amount should not be empty")
        self.assertIsNot(parameters['productinfo'], "", "productinfo should not be empty")
        self.assertLess(len(parameters['txnid']), 35, "Length of txnid is allowed to 35")
        self.assertLess(len(parameters['udf1']), 65, "Length of udf1 is allowed to 65")
        self.assertLess(len(parameters['udf2']), 65, "Length of udf2 is allowed to 65")
        self.assertLess(len(parameters['udf3']), 65, "Length of udf3 is allowed to 65")
        self.assertLess(len(parameters['udf4']), 65, "Length of udf4 is allowed to 65")
        self.assertLess(len(parameters['udf5']), 65, "Length of udf5 is allowed to 65")