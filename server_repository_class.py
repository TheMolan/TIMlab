servers = []

class interface_server_repository:
    def find_server(self,ip):
        return
    def add_server(self,ip):
        return
    def remove_server(self,ip):
        return

class server_repository(interface_server_repository):
    def find_server(self, ip):
        return ip in servers

    def add_server(self, ip):
        if (self.find_server(ip)):
            print('***' + ip + ' is already being monitored***')
            return False
        else:
            servers.append(ip)
            print('***' + ip + ' is added to the monitor***')
            return True

    def remove_server(self, ip):
        if (self.find_server(ip)):
            servers.remove(ip)
            print('***' + ip + ' was removed from the monitor***')
            return True
        else:
            print('***' + ip + ' is not monitored***')
            return False