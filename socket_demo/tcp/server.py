"""
server.py
"""
import socket


BUFFER_SIZE = 1024


def main():
    """
    :return:
    """
    s = socket.socket()
    print("socket created successfully")

    port = 12345

    s.bind(('', port))
    print("socket binded to %s" %(port))

    s.listen(5)
    print("socket is listening")

    while True:
        print("here at start")

        c, addr = s.accept()
        print("'Got connection from", addr)
        rec_msg = c.recv(BUFFER_SIZE)
        print("rec:", rec_msg)

        sent_msg = 'Thank you for connecting'.encode()
        c.send(sent_msg)
        print("sent:", sent_msg)

        c.close()
        print("\n\n")

main()
