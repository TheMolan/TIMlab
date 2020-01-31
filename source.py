import datetime
from random import randrange
import interfaces

servers = []
logs = []


class info_sender(interfaces.interface_info_sender):
    def send(self, data):
        print(data)
        return


class server_log_repository(interfaces.interface_server_log_repository):
    def _check(self, ip):
        for log in logs:
            if log['ip'] == ip:
                return True  # найдена таблица с log
        return False  # не найдена

    def _log_position(self, ip):
        indx = 0
        for log in logs:
            if log['ip'] == ip:
                return indx
            indx += 1

    def find_logs(self, ip):
        return logs

    def add_logs(self, ip, log):
        if not self._check(ip):  # если нет такой таблицы то добавляем новый ip в  логи
            logs.append({'ip': ip})
            logs[self._log_position(ip)][0] = log
        else:  # если есть то просто добавляем логи
            logpos = self._log_position(ip)
            logs[logpos][len(logs[logpos]) - 1] = log
        return


class server_repository(interfaces.interface_server_repository):

    def server_position(self, ip):
        return servers.index(ip)

    def find_server(self, ip):
        return ip in servers

    def add_server(self, ip):
        if (self.find_server(ip)):
            print("***This server is already being monitored***")
        else:
            servers.append(ip)

    def remove_server(self, ip):
        if (self.find_server(ip)):
            servers.remove(ip)
        else:
            print("***This server is not monitored***")


class addserver_command(interfaces.executor):
    def execute(self, query):
        self.repos.add_server(query['ip'])


class removeserver_command(interfaces.executor):
    def execute(self, query):
        self.repos.remove_server(query['ip'])


class server_information_collector_command(interfaces.executor):  # взять инфу с сервера и отправить в отправитель
    def execute(self, query):
        if query['ip'] in servers:
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


class log_collector_command(interfaces.executor):
    def execute(self, query):
        isender = info_sender()
        isender.send(logs)


class request_receiver(interfaces.interface_request_receiver):
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


request_receiver().receive()

