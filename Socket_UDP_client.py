from socket import socket, AF_INET, SOCK_DGRAM

PORT = 12345
MAX_SIZE = 4096

while True:
    print('what')
    sock = socket(AF_INET, SOCK_DGRAM)
    print('heppen')
    msg = "Hello UDP server"
    sock.sendto(msg.encode('utf-8'), ('localhost', PORT))
    data, addr = sock.recvfrom(MAX_SIZE)
    print("Server says:")
    print(repr(data))
    break