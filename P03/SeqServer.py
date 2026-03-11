#from P01_RAQUEL_MARTÍN.Seq1 import Seq
from P02_RAQUEL_MARTIN.Client0 import Client
from Seq1 import Seq

import socket
from termcolor import colored

seq_list = ["ACGTA", "ACTGA", "GTACT", "GTACT", "TCGAT"]
# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")

connection = 0
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        connection += 1
        print(f"CONNECTION {connection} Client IP,PORT{ client_ip_port}")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        cmd = msg.strip().split(" ",1)
        command = cmd[0]
        if command == "PING":
            response = "OK!"
        elif command == "GET":
            i = cmd[1]
            response = seq_list[int(i)]
        elif command == "INFO":
            seq = Seq(cmd[1])
            count = seq.count()
            response = f"Sequence: {cmd[1]} \nTotal length{len(cmd[1])}"
            for key, value in count.items():
                p = (value / len(cmd[1]) * 100)
                pr = round(p, 2)
                response += f"{key}: {value} ({pr} %)\n"
        elif command == "COMP":
            seq = Seq(cmd[1])
            response = seq.complement()
        elif command == "REV":
            seq = Seq(cmd[1])
            response = seq.reverse()


        color_msg = colored(cmd[0] + " " + "command", "green")
        print(f"{color_msg}")

        cs.send(response.encode())

        cs.close()
        print(response)


