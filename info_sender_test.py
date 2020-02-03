import unittest
from info_sender_class import info_sender


class info_sender_test_class(unittest.TestCase):
    def test_InfoSender(self):
        self.TestSender = info_sender()
        print("Testing sending some info")
        self.assertTrue(self.TestSender.send("DATA"))


