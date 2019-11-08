import socket
import time
time.sleep(5)

HOST = 'localhost'   # The server's hostname or IP address
#HOST = '192.168.1.71'# This is the IP of this PC
PORT = 65432         # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while(1):
        s.sendall(b'Hello, world 1')
        data = s.recv(1024)
        print('Received', repr(data))
        time.sleep(2)
        s.sendall(b'Hello, world 2')
        data = s.recv(1024)
        print('Received', repr(data))

