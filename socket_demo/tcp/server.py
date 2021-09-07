"""
server.py
"""
import socket
from porta import PORT, BUFFER_SIZE


def main():
    """
    :return:
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', PORT))

    s.listen(10)
    i = 0
    c, addr = s.accept()
    rec_msg = c.recv(BUFFER_SIZE)
    while rec_msg:
        print("recv i", i)
        rec_msg = c.recv(BUFFER_SIZE)
        i += 1
    c.close()


main()

