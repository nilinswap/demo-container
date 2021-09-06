""" Client"""
import socket
import time


def main():
    """tcp client main"""
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 12345))
        print("received at client", s.recv(1024).decode())
        time.sleep(5)
        s.close()


main()
