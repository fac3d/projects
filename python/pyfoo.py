#
#
#
#
print("before import")
import math
import socket

def socketConnect():
    HOST = '127.0.0.1'
    #HOST = '144.160.155.69'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print('breaking out')
                    break
                else:
                    print(data)
                
                
        conn.disconnect()

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
    socketConnect()
print("after __name__ guard")
