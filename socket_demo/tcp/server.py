import socket


def main():
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

        c.send('Thank you for connecting'.encode())

        c.close()


main()
