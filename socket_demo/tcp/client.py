""" Client"""
import socket
import time
from porta import PORT, BUFFER_SIZE


def main():
    """tcp client main"""
    i = 0
    start_time = time.time()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', PORT))
    # sent_msg = "message from client {}".format(s.getsockname()).encode()
    # s.send(sent_msg)
    # print("sent: sent to server", sent_msg)
    start_time_ = time.time()
    f = open("/Users/nilinswap/forgit/nilinswap/demo-container/socket_demo/scalability_rules.pdf", "rb")
    print("open", time.time() - start_time_)
    l = f.read(BUFFER_SIZE)
    while l:
        print("sizeof l", len(l))
        s.send(l)
        l = f.read(BUFFER_SIZE)
    s.close()
    # print("rec: received at client", rec_msg)

    #time.sleep(5)

    print("full", time.time() - start_time)


main()
