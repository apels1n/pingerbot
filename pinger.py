import subprocess


class Pinger():
    def __init__(self, host, timeout = None):
        self.__host = host

    def checkHost(self):
        command = ['ping', '-n', '4', self.__host]
        return subprocess.call(command) == 0
