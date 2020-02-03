import unittest
from executor_class import *


class executor_test_class(unittest.TestCase):
    def test_AddserverCommand(self):
        print("Testing adding servers in server list")
        Executor = addserver_command(server_repository())
        self.assertIsNone(Executor.execute({'ip': "127.0.0.1"}))
        Executor = addserver_command(server_repository())
        self.assertIsNone(Executor.execute({'ip': "127.0.0.1"}))
        Executor = addserver_command(server_repository())
        self.assertIsNone(Executor.execute({'ip': "109.27.10.202"}))

    def test_RemoveserverCommandTest(self):
        print("Testing removing servers from server list")
        Executor = removeserver_command(server_repository())
        self.assertIsNone(Executor.execute({'ip': "127.0.0.1"}))
        Executor = removeserver_command(server_repository())
        self.assertIsNone(Executor.execute({'ip': "127.0.0.1"}))

    def test_LogCollectorCommandTest(self):
        print("Testing receiving some logs")
        Executor = log_collector_command(server_log_repository())
        self.assertTrue(Executor.execute({'ip': "109.27.10.202"}))

    def test_ServerInformationCollectorCommandTest(self):
        print("Testing adding some logs")
        Executor = server_information_collector_command(server_log_repository())
        self.assertTrue(Executor.execute({'ip': "109.27.10.202"}))
        Executor = server_information_collector_command(server_log_repository())
        self.assertFalse(Executor.execute({'ip': "127.0.0.1"}))



