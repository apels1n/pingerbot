import subprocess

class Pinger():
    def __init__(self, host, timeout = None):
        self._host = host
        self._timeout = timeout

    def checkHost(self):
        command = ['ping', '-n', '4', self._host]
        return subprocess.call(command) == 0