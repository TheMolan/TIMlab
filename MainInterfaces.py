class interface_info_sender:
    def send(self, data):
        return

class interface_server_log_repository:
    def find_logs(self, ip):
        return
    def add_logs(self, ip, log):
        return

class interface_server_repository:
    def find_server(self,ip):
        return
    def add_server(self,ip):
        return
    def remove_server(self,ip):
        return

class executor():
    def __init__(self, repos):
        self.repos = repos
    def execute(self, query):
        return

class interface_request_receiver:
    def receive(self):
        return