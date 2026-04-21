import http.server
import socketserver
import termcolor
from pathlib import Path
# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'white')

        try:
            file_name = self.path.lstrip("/") # no tienes que definir el path porque es algo que ya viene en lo de handler, y es simplemente el html que quiere el client

                                              #escribes una l de left sino te quiataría las / de la derecha también

            if file_name == "":
                file_name = "index.html"

            path = Path("html") / file_name #NO ESTAS DIVIDIENDO es lo mismo que poner "html/" + file_name lo que pasa que de esa forma tendrías que poenr lo de r
                                            # y nosotros usamos path
            contents = path.read_text()

            self.send_response(200)

        except FileNotFoundError:
            path = Path("html") / "error.html"
            contents = path.read_text()

            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
