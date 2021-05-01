"""
This module enables the socket
to initialize the webserver.
"""
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)


class SocketConfig:
    ADDRESS = ''
    PORT = None
    CONNECTION_LIMIT = None

class Server(SocketConfig):
    def __init__(self, address='', port=80, limit=5):
        # Redefine socket settings
        self.PORT = port
        self.ADDRESS = address
        self.CONNECTION_LIMIT = limit
        # init socket
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        # Define port and address
        self.tcp_socket.bind((self.ADDRESS, self.PORT))
        # Define connection limit
        self.tcp_socket.listen(self.CONNECTION_LIMIT)

    def read(self):
        while True:
            self.connection, address = self.tcp_socket.accept()
            print('new connection - %s' % str(address))

            # Read request
            request = self.connection.recv(1024)
            request = str(request)
            print('request - %s' % request)
            return request

    def send(self, data) -> None:
        self.connection.send('HTTP/1.1 200 OK\n')
        self.connection.send('Content-Type: text/html\n')
        self.connection.send('Connection: close\n\n')
        self.connection.sendall(data)
        self.connection.close()

