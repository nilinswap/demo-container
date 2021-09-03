import socket
import time

def main():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        v = s.connect(('127.0.0.1', 12345))
        print("received at client1", s.recv(1024).decode())
        time.sleep(5)
        s.close()


main()
