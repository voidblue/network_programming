import socket

HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 256



if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter hostname [%s]: " %HOST) or HOST
    port = input("Enter port [%s]: " %PORT) or PORT
    sock_addr = (host, int(port))
    client_sock.connect(sock_addr)
    payload = 'GET TIME'
    try:
        while True:
            client_sock.send(payload.encode('utf-8'))
            data = client_sock.recv(BUFSIZE)
            print(repr(data))
            more = input("Want to send more data to server[y/n]:")
            if more.lower() == 'y':
                payload = input("Enter payload: ")
            else:
                break
    except KeyboardInterrupt:
        print("Exited by user")
        client_sock.close()