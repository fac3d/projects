#!/usr/bin/env python3

import socket
#import fcntl, termios, array, math


HOST = 'localhost'     # Standard loopback interface address (localhost)
#HOST = '192.168.1.71' # This is the IP of this PC
PORT = 65432           # Port to listen on (non-privileged ports are > 1023)
i = 0
data = 'Frank HP Windows Heartbeat', str(i)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            #fcntl.ioctl(s,termios.FIONREAD, sock_size)
            #count = ceil(sock_size[0] / float(BUF_SIZE))
            #print("Socket size: {} and count: {}".format(sock_size[0], count))
            i = i + 1
            data = conn.recv(1024)
            l=len(data)
            if(l != 0):
                print ('received data is ',data,'length is',l,'count is',i)
                data = (b'Frank HP Windows Heartbeat')
                #if not data:
             #   break
                conn.sendall(data)
