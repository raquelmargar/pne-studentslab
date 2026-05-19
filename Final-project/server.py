import http.client
import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
import jinja2 as j
from Seq1 import Seq

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def send_json_response(self, data):
        json_string = json.dumps(data)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(str.encode(json_string)))
        self.end_headers()
        self.wfile.write(str.encode(json_string))

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

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

                if "json" in arguments and arguments["json"][0] == "1":
                    self.send_json_response({"limit": limit, "species": species_list})
                    return

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
                    species = species.replace(" ", "%20")
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

                        if "json" in arguments and arguments["json"][0] == "1":
                            self.send_json_response({"chromosomes": chromosomes_list})
                            return

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
                    species = species.replace(" ", "%20")
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

                        if "json" in arguments and arguments["json"][0] == "1":
                            self.send_json_response({"length": length})
                            return

                        html_file = Path("html/length.html")
                        contents = html_file.read_text()

                        template = j.Template(contents)
                        contents = template.render(length=length)

                        self.send_response(200)
                    else:
                        raise Exception()
                else:
                    raise Exception()

            elif path == "/geneLookup":
                if "gene" in arguments:
                    gene = arguments["gene"][0]
                    conn = http.client.HTTPConnection("rest.ensembl.org")
                    conn.request("GET", f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json")
                    response = conn.getresponse()

                    if response.status == 200:
                        data = response.read().decode("utf-8")
                        gene_data = json.loads(data)
                        gene_id = gene_data.get("id")

                        if "json" in arguments and arguments["json"][0] == "1":
                            self.send_json_response({"gene": gene, "id": gene_id})
                            return

                        html_file = Path("html/lookup.html")
                        contents = html_file.read_text()
                        template = j.Template(contents)
                        contents = template.render(gene=gene, id=gene_id)
                        self.send_response(200)
                    else:
                        raise Exception()
                else:
                    raise Exception()

            elif path == "/geneSeq":
                if "gene" in arguments:
                    gene = arguments["gene"][0]
                    conn = http.client.HTTPConnection("rest.ensembl.org")
                    conn.request("GET", f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json")
                    response = conn.getresponse()

                    if response.status == 200:
                        gene_data = json.loads(response.read().decode("utf-8"))
                        gene_id = gene_data.get("id")

                        conn2 = http.client.HTTPConnection("rest.ensembl.org")
                        conn2.request("GET", f"/sequence/id/{gene_id}?content-type=application/json")
                        response2 = conn2.getresponse()

                        if response2.status == 200:
                            seq_data = json.loads(response2.read().decode("utf-8"))
                            sequence = seq_data.get("seq")

                            if "json" in arguments and arguments["json"][0] == "1":
                                self.send_json_response({"gene": gene, "sequence": sequence})
                                return

                            html_file = Path("html/Seq.html")
                            contents = html_file.read_text()
                            template = j.Template(contents)
                            contents = template.render(gene=gene, sequence=sequence)
                            self.send_response(200)
                        else:
                            raise Exception()
                    else:
                        raise Exception()


            elif path == "/geneInfo":
                if "gene" in arguments:
                    gene = arguments["gene"][0]
                    conn = http.client.HTTPConnection("rest.ensembl.org")
                    conn.request("GET", f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json")
                    response = conn.getresponse()

                    if response.status == 200:
                        gene_data = json.loads(response.read().decode("utf-8"))
                        gene_id = gene_data.get("id")
                        chromo = gene_data.get("seq_region_name")
                        start = gene_data.get("start")
                        end = gene_data.get("end")
                        length = int(end) - int(start) + 1

                        if "json" in arguments and arguments["json"][0] == "1":
                            self.send_json_response(
                                {"gene": gene, "chromo": chromo, "start": start, "end": end, "length": length,
                                 "id": gene_id})
                            return

                        html_file = Path("html/info.html")
                        contents = html_file.read_text()
                        template = j.Template(contents)
                        contents = template.render(gene=gene, chromo=chromo, start=start, end=end, length=length,
                                                   id=gene_id)
                        self.send_response(200)
                    else:
                        raise Exception()
                else:
                    raise Exception()


            elif path == "/geneCalc":
                if "gene" in arguments:
                    gene = arguments["gene"][0]
                    conn = http.client.HTTPConnection("rest.ensembl.org")
                    conn.request("GET", f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json")
                    response = conn.getresponse()

                    if response.status == 200:
                        gene_data = json.loads(response.read().decode("utf-8"))
                        gene_id = gene_data.get("id")
                        conn2 = http.client.HTTPConnection("rest.ensembl.org")
                        conn2.request("GET", f"/sequence/id/{gene_id}?content-type=application/json")
                        response2 = conn2.getresponse()

                        if response2.status == 200:
                            seq_data = json.loads(response2.read().decode("utf-8"))
                            sequence = seq_data.get("seq")
                            s = Seq(sequence)
                            total_len = s.len()
                            bases_count = s.count()

                            if total_len > 0:
                                perc_a = round((bases_count['A'] / total_len) * 100, 2)
                                perc_c = round((bases_count['C'] / total_len) * 100, 2)
                                perc_g = round((bases_count['G'] / total_len) * 100, 2)
                                perc_t = round((bases_count['T'] / total_len) * 100, 2)

                            else:
                                perc_a = 0
                                perc_c = 0
                                perc_g = 0
                                perc_t = 0

                            if "json" in arguments and arguments["json"][0] == "1":
                                self.send_json_response({
                                    "gene": gene, "length": total_len,
                                    "perc_A": perc_a, "perc_C": perc_c,
                                    "perc_G": perc_g, "perc_T": perc_t
                                })
                                return

                            html_file = Path("html/calculations.html")
                            contents = html_file.read_text()
                            template = j.Template(contents)
                            contents = template.render(gene=gene, length=total_len, perc_A=perc_a, perc_C=perc_c,
                                                       perc_G=perc_g, perc_T=perc_t)
                            self.send_response(200)

                        else:
                            raise Exception()
                    else:
                        raise Exception()

            elif path == "/geneList":
                if "chromo" in arguments and "start" in arguments and "end" in arguments:
                    chromo = arguments["chromo"][0]
                    start = arguments["start"][0]
                    end = arguments["end"][0]

                    conn = http.client.HTTPConnection("rest.ensembl.org")
                    conn.request("GET",
                                 f"/overlap/region/homo_sapiens/{chromo}:{start}-{end}?feature=gene;content-type=application/json")
                    response = conn.getresponse()

                    if response.status == 200:
                        overlap_data = json.loads(response.read().decode("utf-8"))
                        genes_list = []

                        for item in overlap_data:
                            if "external_name" in item:
                                genes_list.append(item["external_name"])

                        if "json" in arguments and arguments["json"][0] == "1":
                            self.send_json_response({"genes": genes_list, "chromo": chromo, "start": start, "end": end})
                            return

                        html_file = Path("html/list.html")
                        contents = html_file.read_text()
                        template = j.Template(contents)
                        contents = template.render(genes=genes_list, chromo=chromo, start=start, end=end)
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