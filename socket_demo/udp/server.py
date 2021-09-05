"""
server.py

"""

import socket

BUFFER_SIZE = 1024

GLOBAL_COUNTER = 0

def main():
    """
    main function
    :return:
    """

    UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_port = 1234
    UDPServer.bind(('', server_port))

    print("server has started listening")
    server_message = 'Hey, This is server'.encode()
    global GLOBAL_COUNTER
    while True:
        AddressDataPair = UDPServer.recvfrom(BUFFER_SIZE)
        clientAddress = AddressDataPair[1]
        clientMessage = AddressDataPair[0]
        server_message = ('Hey, This is server ' + str(GLOBAL_COUNTER)).encode()
        print("recieved from", clientAddress, " , Data:", clientMessage)
        UDPServer.sendto(server_message, clientAddress)
        GLOBAL_COUNTER += 1

main()

