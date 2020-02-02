logs = []

class interface_server_log_repository:
    def find_logs(self, ip):
        return
    def add_logs(self, ip, log):
        return

class server_log_repository(interface_server_log_repository):
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