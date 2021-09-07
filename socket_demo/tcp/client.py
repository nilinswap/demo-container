""" Client"""
import socket
import time
from porta import PORT, BUFFER_SIZE


def main():
    """tcp client main"""
    i = 0
    start_time = time.time()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print("this part done da 1")
    s.connect(('65.1.131.84', PORT))
    # print("this part done da")
    # sent_msg = "message from client {}".format(s.getsockname()).encode()
    # s.send(sent_msg)
    # print("sent: sent to server", sent_msg)
    f = open("/Users/nilinswap/forgit/nilinswap/demo-container/socket_demo/scalability_rules.pdf", "rb")
    l = f.read(BUFFER_SIZE)
    print("l", l)
    while l:
        print("sizeof l", len(l))
        s.send(l)
        l = f.read(BUFFER_SIZE)
    s.close()
    # print("rec: received at client", rec_msg)

    #time.sleep(5)

    print("full", time.time() - start_time)


main()
