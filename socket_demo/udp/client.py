"""
client.py
"""
import socket
import time

BUFFER_SIZE = 1024


def main():
    """
    client's main
    :return:
    """

    UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_ip = '127.0.0.1'
    server_port = 1234
    clientMessage = "Hi, this is client.".encode()
    while True:

        UDPClient.sendto(clientMessage, (server_ip, server_port))

        serverMessage = UDPClient.recvfrom(BUFFER_SIZE)
        print("message from server", serverMessage[0])
        time.sleep(5)

main()

