import unittest
from executor_class import *

class executor_test_class(unittest.TestCase):
    def __init__(self):
        self.ExecutorFirstTestQuery = { 'ip': "127.0.0.1" }
        self.ExecutorSecondTestQuery = {'ip': "109.27.10.202"}
    def AddserverCommandTest(self):
        print("Testing adding servers in server list")
        Executor = addserver_command(server_repository())
        Executor.execute(self.ExecutorFirstTestQuery)
        Executor = addserver_command(server_repository())
        Executor.execute(self.ExecutorFirstTestQuery)
        Executor = addserver_command(server_repository())
        Executor.execute(self.ExecutorSecondTestQuery)
    def RemoveserverCommandTest(self):
        print("Testing removing servers from server list")
        Executor = removeserver_command(server_repository())
        Executor.execute(self.ExecutorFirstTestQuery)
        Executor = removeserver_command(server_repository())
        Executor.execute(self.ExecutorFirstTestQuery)
    def ServerInformationCollectorCommandTest(self):
        print("Testing adding some logs")
        Executor = server_information_collector_command(server_log_repository())
        self.assertTrue(Executor.execute(self.ExecutorSecondTestQuery))
        Executor = server_information_collector_command(server_log_repository())
        self.assertFalse(Executor.execute(self.ExecutorFirstTestQuery))
    def LogCollectorCommandTest(self):
        print("Testing receiving some logs")
        Executor = log_collector_command(server_log_repository())
        self.assertTrue(Executor.execute(self.ExecutorSecondTestQuery))

Test = executor_test_class()
Test.AddserverCommandTest()
Test.RemoveserverCommandTest()
Test.ServerInformationCollectorCommandTest()
Test.LogCollectorCommandTest()
print("Done!")
