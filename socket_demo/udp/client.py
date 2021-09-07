"""
client.py
"""
import socket
import time
import porta


def main():
    """
    client's main
    :return:
    """

    start_time = time.time()

    UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_ip = '127.0.0.1'
    server_port = porta.PORT
    f = open("/Users/nilinswap/forgit/nilinswap/demo-container/socket_demo/scalability_rules.pdf", "rb")
    l = f.read(porta.BUFFER_SIZE)
    while l:
        #print("sizeof l", len(l))
        UDPClient.sendto(l, (server_ip, server_port))
        l = f.read(porta.BUFFER_SIZE)
    UDPClient.close()

    print("full", time.time() - start_time)

main()

