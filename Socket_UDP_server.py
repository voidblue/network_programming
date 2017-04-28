from socket import socket, AF_INET, SOCK_DGRAM


maxsize = 4096

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('',12345))
while True:
    print('server open')
    data, addr = sock.recvfrom(maxsize)
    resp = "UDP server sending data"
    sock.sendto(resp.encode('utf-8'),addr)
    print(repr(data))
#FTP와 SSH를 서버와 클라이언트로 해서 짝지어서 해보고 동작확인 해보고, wireshark로 사용해서 돌려볼것