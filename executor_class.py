import datetime
from random import randrange
from info_sender_class import info_sender
import server_repository_class
import server_log_repository_class

class executor():
    def __init__(self, repos):
        self.repos = repos
    def execute(self, query):
        return


class addserver_command(executor):
    def execute(self, query):
        self.repos.add_server(query['ip'])


class removeserver_command(executor):
    def execute(self, query):
        self.repos.remove_server(query['ip'])


class server_information_collector_command(executor):  #
    def execute(self, query):
        if query['ip'] in server_repository_class.servers:###
            timelog = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            cpulog = randrange(50, 100, 10)
            log = {
                'timelog': timelog,
                'cpulog': cpulog}
            #            print(timelog, ' ', query['ip'], ' ', cpulog)
            self.repos.add_logs(query['ip'], log)
            isender = info_sender()
            isender.send(log)
        else:
            print("***This server is not monitored***")


class log_collector_command(executor):
    def execute(self, query):
        isender = info_sender()
        isender.send(server_log_repository_class.logs)###