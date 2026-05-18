import http.client
import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
import jinja2 as j

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file

        try:
            url_path = urlparse(self.path)
            path = url_path.path  # te devuelve el path p.ej "/echo"
            arguments = parse_qs(url_path.query)  # te devuelve el mensaje en forma de diccionario

            if path == "/":
                html_file = Path("html/mainpage.html")
                contents = html_file.read_text()
                self.send_response(200)

            elif path == "/listSpecies":
                conn = http.client.HTTPConnection("rest.ensembl.org")
                conn.request("GET", f"/info/species?content-type=application/json")

                response = conn.getresponse()
                data = response.read().decode("utf-8")
                species_data = json.loads(data)

                if "limit" in arguments:
                    limit = int(arguments["limit"][0])
                else:
                    limit = len(species_data["species"])

                species_list = []

                counter = 0

                for sp in species_data["species"]:

                    if counter < limit:
                        species_list.append(sp["display_name"])

                        counter += 1

                html_file = Path("html/limitation.html")

                contents = html_file.read_text()

                template = j.Template(contents)

                contents = template.render(
                    total=len(species_data["species"]),
                    limit=limit,
                    species=species_list
                )

                self.send_response(200)


            elif path == "/karyotype":

                if "species" in arguments:

                    species = arguments["species"][0]
                    species = species.lower().replace(" ", "_")
                    conn = http.client.HTTPConnection("rest.ensembl.org")
                    conn.request("GET", f"/info/assembly/{species}?content-type=application/json")
                    response = conn.getresponse()

                    if response.status == 200:
                        data = response.read().decode("utf-8")
                        species_data = json.loads(data)
                        chromosomes_list = []

                        if "karyotype" in species_data and species_data["karyotype"]:
                            chromosomes_list = species_data["karyotype"]

                        elif "top_level_region" in species_data:
                            for region in species_data["top_level_region"]:
                                if region.get("coord_system") == "chromosome" or region.get("is_chromosome") == 1:
                                    chromosomes_list.append(region.get("name"))

                        html_file = Path("html/karyotype.html")
                        contents = html_file.read_text()
                        template = j.Template(contents)
                        contents = template.render(
                            chromosomes=chromosomes_list
                        )
                        self.send_response(200)

                    else:
                        raise Exception()
                else:
                    raise Exception()

            elif path == "/chromosomeLength":
                if "species" in arguments and "chromo" in arguments:
                    species = arguments["species"][0]
                    species = species.lower().replace(" ", "_")
                    chromosome = arguments["chromo"][0]

                    conn = http.client.HTTPConnection("rest.ensembl.org")
                    conn.request("GET", f"/info/assembly/{species}?content-type=application/json")

                    response = conn.getresponse()

                    if response.status == 200:
                        data = response.read().decode("utf-8")
                        species_data = json.loads(data)

                        length = None

                        if "top_level_region" in species_data:
                            for region in species_data["top_level_region"]:
                                if region.get("name") == chromosome:
                                    length = region.get("length")
                                    break

                        html_file = Path("html/length.html")
                        contents = html_file.read_text()

                        template = j.Template(contents)
                        contents = template.render(length=length)

                        self.send_response(200)
                    else:
                        raise Exception()
                else:
                    raise Exception()
            else:
                raise Exception()

        except FileNotFoundError:
            html_file = Path("html/error.html")
            contents = html_file.read_text()
            self.send_response(404)

        except Exception:
            html_file = Path("html/error.html")
            contents = html_file.read_text()
            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
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