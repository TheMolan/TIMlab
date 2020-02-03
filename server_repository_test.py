import unittest
from server_repository_class import server_repository


class server_repository_test_class(unittest.TestCase):

    def test_AddingToList(self):
        print("Testing adding servers in server list")
        self.assertTrue(server_repository().add_server("127.0.0.1"))
        self.assertFalse(server_repository().add_server("127.0.0.1"))
        self.assertTrue(server_repository().add_server("172.16.254.1"))

    def test_RemovingFromList(self):
        print("Testing removing servers from server list")
        self.assertTrue(server_repository().remove_server("127.0.0.1"))
        self.assertFalse(server_repository().remove_server("127.0.0.1"))
        self.assertTrue(server_repository().remove_server("172.16.254.1"))

    def test_FindingInList(self):
        print("Testing adding 59.47.213.121 to server list and finding it")
        self.assertTrue(server_repository().add_server("59.47.213.121"))
        self.assertTrue(server_repository().find_server("59.47.213.121"))



