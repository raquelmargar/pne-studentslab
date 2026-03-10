import socket
from termcolor import colored

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.97" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")

connection = 0
client_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        connection += 1
        print(f"CONNECTION {connection} Client IP,PORT{ client_ip_port}")
        client_list.append(client_ip_port)

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        color_msg = colored(msg,"green")

        # -- Print the received message
        print(f"Message received: {color_msg}")

        # -- Send a response message to the client
        response = f"ECHO: {msg}"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())
        if len(client_list) == 5:
            for j,i in enumerate(client_list):
                print(f"Client {j}: {i}")
            break

        # -- Close the data socket
        cs.close()