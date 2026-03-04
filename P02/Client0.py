class Client:
    def __init__(self, ip, port):
       self.ip = ip
       self.port = port

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def ping(self):
        print("OK")

    def talk(msg):
        PORT = 8081
        IP = "212.128.255.91"

        while True:
            ms = input("Enter your message:")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((IP, PORT))

            s.send(str.encode(ms))
            s.close()


