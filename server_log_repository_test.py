import unittest
from server_log_repository_class import server_log_repository

class server_log_repository_test_class(unittest.TestCase):
    def __init__(self):
        self.TestServerLogRepos = server_log_repository()
        self.Newip = "New LOGS"
        self.Oldip = "Old LOGS"
    def AddingToLogsTest(self):
        print("Testing adding some logs")
        self.assertTrue(self.TestServerLogRepos.add_logs("240.5.200.56",self.Newip))
        self.assertFalse(self.TestServerLogRepos.add_logs("240.5.200.56",self.Oldip))
        self.assertTrue(self.TestServerLogRepos.add_logs("127.0.0.1",self.Newip))
        self.assertFalse(self.TestServerLogRepos.add_logs("127.0.0.1",self.Oldip))
    def ReceivingFromLogsTest(self):
        print("Testing receiving some logs")
        print(self.TestServerLogRepos.find_logs())

Test = server_log_repository_test_class()
Test.AddingToLogsTest()
Test.ReceivingFromLogsTest()
print("Done!")