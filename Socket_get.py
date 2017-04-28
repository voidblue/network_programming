from socket import *
import socket
import sys

Host = '220.149.42.76'
Port =  12345
Bufsize = 4096
Addr = (Host,Port)

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(Addr)
    while True:
        data = 'GET / HTTP/1.0\r\n\r\n'
        print(data)
        if not data:
            break
        client_socket.send(data.encode('utf-8'))
        data = client_socket.recv(Bufsize)
        print(data.decode('utf-8'))
        if not data:
            break
    client_socket.close()
