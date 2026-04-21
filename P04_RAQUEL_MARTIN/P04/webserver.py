import socket
import termcolor

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080

def process_client(cs):
    # -- Receive the request message
    req_raw = cs.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Extract the requested path
    path = req_line.split(" ")[1]

    if path == "/info/A":
        with open("html/info/A.html", "r", encoding="utf-8") as f:
            body = f.read()
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response_msg = status_line + header + "\n" + body
        cs.send(response_msg.encode())

    elif path == "/info/C":
        with open("html/info/C.html", "r", encoding="utf-8") as f:
            body = f.read()
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response_msg = status_line + header + "\n" + body
        cs.send(response_msg.encode())

    elif path == "/info/G":
        with open("html/info/G.html", "r", encoding="utf-8") as f:
            body = f.read()
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response_msg = status_line + header + "\n" + body
        cs.send(response_msg.encode())

    elif path == "/info/T":
        with open("html/info/T.html", "r", encoding="utf-8") as f:
            body = f.read()
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response_msg = status_line + header + "\n" + body
        cs.send(response_msg.encode())

    elif path == "/":
        with open("html/index.html", "r", encoding="utf-8") as f:
            body = f.read()
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response_msg = status_line + header + "\n" + body
        cs.send(response_msg.encode())

    else:
        with open("html/error.html", "r", encoding="utf-8") as f:
            body = f.read()
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response_msg = status_line + header + "\n" + body
        cs.send(response_msg.encode())

# -------------- MAIN PROGRAM
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("Server running at http://127.0.0.1:8080/")
# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:
        # Service the client
        process_client(cs)
        # Close the client socket
        cs.close()


