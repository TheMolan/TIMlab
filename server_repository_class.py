servers = []

class interface_server_repository:
    def find_server(self,ip):
        return
    def add_server(self,ip):
        return
    def remove_server(self,ip):
        return

class server_repository(interface_server_repository):
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