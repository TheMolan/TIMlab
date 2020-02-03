import unittest
from server_log_repository_class import server_log_repository


class server_log_repository_test_class(unittest.TestCase):

    def test_AddingToLogs(self):
        print("Testing adding some logs")
        self.assertTrue(server_log_repository().add_logs("240.5.200.56", "New LOGS"))
        self.assertFalse(server_log_repository().add_logs("240.5.200.56", "Old LOGS"))
        self.assertTrue(server_log_repository().add_logs("127.0.0.1", "New LOGS"))
        self.assertFalse(server_log_repository().add_logs("127.0.0.1", "Old LOGS"))

    def test_ReceivingLogs(self):
        print("Testing receiving some logs")
        self.assertIsNotNone(server_log_repository().find_logs())



