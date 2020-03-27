from sys import argv
import sys
import socket
import json
import psutil
import os
import wmi

class ClientError(Exception):
    """class client exception"""
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            print(err)

    def _send(self, data):
        try:
            self.connection.sendall(data.encode())
        except ConnectionError as err:
            raise ClientError("Error sending data to socket", err)

    def _read(self):
        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
            except ConnectionError as err:
                raise ClientError("Error reading data from socket", err)

    def put(self, data):
        self._send(data)

    def close(self):

        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError("Error. Do not close the connection", err)


if __name__ == "__main__":
    disks = {}
    #_, address, port = argv
    #print(os.name, sys.platform, psutil.disk_partitions())
    for disk in psutil.disk_partitions():
        disks[disk[1]] = psutil.disk_usage(disk[1]).total/(1024**3)
    #client = Client(address, port)
    #client.put(json.dumps(some_data))
