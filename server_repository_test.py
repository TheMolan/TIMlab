import unittest
from server_repository_class import server_repository

class server_repository_test_class(unittest.TestCase):
    def __init__(self):
        self.TestServerRepos = server_repository()
    def AddingToListTest(self):
        print("Testing adding servers in server list")
        self.assertTrue(self.TestServerRepos.add_server("127.0.0.1"))
        self.assertFalse(self.TestServerRepos.add_server("127.0.0.1"))
        self.assertTrue(self.TestServerRepos.add_server("172.16.254.1"))
    def RemovingFromListTest(self):
        print("Testing removing servers from server list")
        self.assertTrue(self.TestServerRepos.remove_server("127.0.0.1"))
        self.assertFalse(self.TestServerRepos.remove_server("127.0.0.1"))
        self.assertTrue(self.TestServerRepos.remove_server("172.16.254.1"))
    def FindingInList(self):
        print("Testing adding 59.47.213.121 to server list and finding it")
        self.assertTrue(self.TestServerRepos.add_server("59.47.213.121"))
        self.assertTrue(self.TestServerRepos.find_server("59.47.213.121"))

Test = server_repository_test_class()
Test.AddingToListTest()
Test.RemovingFromListTest()
Test.FindingInList()
print("Done!")