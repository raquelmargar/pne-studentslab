import http.server
import socketserver
import termcolor
from pathlib import Path
import urllib.parse

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'white')

        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        try:

            # ---------------- PING ----------------
            if path == "/ping":
                contents = """
                <html>
                    <body>
                        <h1>Ping OK!</h1>
                        <p>The SEQ2 server is running...</p>
                        <a href="/">Main page</a>
                    </body>
                </html>
                """
                self.send_response(200)

            # ---------------- GET ----------------
            elif path.startswith("/get"):

                seq = "0"

                if "seq=" in self.path:
                    seq = self.path.split("seq=")[1].split("&")[0]

                contents = f"""
                <html>
                    <body>
                        <h1>Sequence number {seq}</h1>
                        <p>This is sequence {seq}</p>
                        <a href="/">Main page</a>
                    </body>
                </html>
                """

                self.send_response(200)

            # ---------------- GENE ----------------
            elif path.startswith("/gene"):

                gene = "U5"

                if "gene=" in self.path:
                    gene = self.path.split("gene=")[1].split("&")[0]

                # aquí deberías tener tu diccionario real en seq1
                gene_info = "Gene information not loaded"

                contents = f"""
                <html>
                    <body>
                        <h1>Gene: {gene}</h1>
                        <p>{gene_info}</p>
                        <a href="/">Main page</a>
                    </body>
                </html>
                """

                self.send_response(200)

            # ---------------- OPERATION ----------------
            elif path.startswith("/operation"):

                seq = ""
                op = "1"

                if "seq=" in self.path:
                    seq = self.path.split("seq=")[1].split("&")[0]

                if "op=" in self.path:
                    op = self.path.split("op=")[1].split("&")[0]

                # INFO
                if op == "1":
                    result = f"Sequence info: {seq}"

                # COMPLEMENT
                elif op == "2":
                    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
                    result = "".join([complement.get(b, b) for b in seq])

                # REVERSE
                elif op == "3":
                    result = seq[::-1]

                else:
                    result = "Invalid operation"

                contents = f"""
                <html>
                    <body>
                        <h1>Result</h1>
                        <p>{result}</p>
                        <a href="/">Main page</a>
                    </body>
                </html>
                """

                self.send_response(200)

            # ---------------- INDEX / FILES ----------------
            else:

                file_name = path.strip("/")

                if file_name == "":
                    file_name = "index.html"

                file_path = Path("html") / file_name
                contents = file_path.read_text()

                self.send_response(200)

        # ---------------- ERROR ----------------
        except FileNotFoundError:
            file_path = Path("html/error.html")
            contents = file_path.read_text()
            self.send_response(404)

        # ---------------- HEADERS ----------------
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()

        self.wfile.write(contents.encode())


# ---------------- SERVER ----------------
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by user")
        httpd.server_close()