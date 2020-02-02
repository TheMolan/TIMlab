from executor_class import *#addserver_command, removeserver_command, server_information_collector_command, log_collector_command
from server_repository_class import *#server_repository
from server_log_repository_class import *#server_log_repository

class interface_request_receiver:
    def receive(self):
        return

class request_receiver(interface_request_receiver):
    def validate(self, command):
        if (
                command != 'addserver' and
                command != 'removeserver' and
                command != 'serverinfo' and
                command != 'sendlogs'
        ):
            print("Unknown command")
            return False
        return True

    def receive(self):
        while 1:
            command = input("Command: ")
            if self.validate(command):
                if (command == 'addserver'):
                    ip = input("Enter server ip: ")
                    query = {
                        'ip': ip
                    }
                    executor = addserver_command(server_repository())
                if (command == 'removeserver'):
                    ip = input("Enter server ip: ")
                    query = {
                        'ip': ip
                    }
                    executor = removeserver_command(server_repository())
                if (command == 'serverinfo'):
                    ip = input("Enter server ip: ")
                    query = {
                        'ip': ip
                    }
                    executor = server_information_collector_command(server_log_repository())
                if (command == 'sendlogs'):
                    query = []
                    executor = log_collector_command(server_log_repository())
                executor.execute(query)

if __name__ == '__main__':
	request_receiver().receive()