import unittest
from info_sender_class import info_sender

class info_sender_test_class(unittest.TestCase):
    def __init__(self):
        self.TestSender = info_sender()
    def InfoSenderTest(self):
        print("Testing sending some info")
        self.assertTrue(self.TestSender.send("DATA"))

Test = info_sender_test_class()
Test.InfoSenderTest()
print("Done!")
