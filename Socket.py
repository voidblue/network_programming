from socket import *
import socket
import sys



if __name__ ==  '__main__':
    try:
        sock = socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0)
        # 소켓 종류                 TCP사용 , UDP는 DGRAM   proto = protocol ??
    except socket.error as err:
        print("Failed to create a socket")
        print('Reason : {}'.format(err))
        sys.exit()
    print('socket created')

    target_host = input("Enter the target host name to connect : ")
    target_port = input("Enter the target host port to connect : ")

    try:
        sock.connect((target_host,int(target_port)))
        print("connected host {}, on port {} ".format(target_host,target_port))
        sock.shutdown(2)
    except socket.error as err:
        print("Failed to connect to {} on port {}".format(target_host,target_port))
        print("Reason: %s" % str(err))
        sys.exit()


