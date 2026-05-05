import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file

        try:
            url_path = urlparse(self.path)
            path = url_path.path # te devuelve el path p.ej "/echo"
            arguments = parse_qs(url_path.query) # te devuelve el mensaje en forma de diccionario

            if path == "/":



            elif path == "/listSpecies":
                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", f"info/species?content-type=application/json")

                response = conn.getresponse()
                data = response.read().decode("utf-8")
                species_data = json.loads(data)

            elif path == "/karyotype":
                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", f"info/assembly/homo_sapiens?content-type=application/json")

                response = conn.getresponse()
                data = response.read().decode("utf-8")
                species_data = json.loads(data)

            elif path == "/chromosomeLength":
                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", f"info/assembly/homo_sapiens?content-type=application/json")

                response = conn.getresponse()
                data = response.read().decode("utf-8")
                species_data = json.loads(data)

        except FileNotFoundError:
            path = Path("error.html")
            contents = path.read_text()

            self.send_response(404)
           # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(str.encode(contents))

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
