import unittest
from request_receiver_class import *

class request_receiver_test_class(unittest.TestCase):
    def ValidateTest(self):
        print("Testing command validation")
        RequestReceiverTest = request_receiver()
        self.assertTrue(RequestReceiverTest.validate("addserver"))
        self.assertTrue(RequestReceiverTest.validate("removeserver"))
        self.assertTrue(RequestReceiverTest.validate("serverinfo"))
        self.assertTrue(RequestReceiverTest.validate("sendlogs"))
        self.assertTrue(RequestReceiverTest.validate("stop"))
        self.assertFalse(RequestReceiverTest.validate("someothercommand"))
    def ReceiveTest(self):
        print("Testing receiving commands")
        RequestReceiverTest = request_receiver()
        RequestReceiverTest.receive()

Test = request_receiver_test_class()
Test.ValidateTest()
Test.ReceiveTest()