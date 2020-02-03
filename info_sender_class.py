class interface_info_sender:
    def send(self, data):
        return

class info_sender(interface_info_sender):
    def send(self, data):
        print(data)
        return True