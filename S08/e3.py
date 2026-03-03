import socket

PORT = 8081
IP = "212.128.255.91"

while True:
    ms = input("Enter your message:")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, PORT))

    s.send(str.encode(ms))
    s.close()
