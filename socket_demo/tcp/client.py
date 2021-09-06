""" Client"""
import socket
import time


def main():
    """tcp client main"""
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 12345))

        sent_msg = "message from client {}".format(s.getsockname());

        s.send(sent_msg)

        print("sent: sent to server", sent_msg)
        rec_msg = s.recv(1024).decode()
        print("rec: received at client", rec_msg)

        time.sleep(5)
        s.close()


main()
