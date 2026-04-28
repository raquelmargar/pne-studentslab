import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552"
PARAMS = "?content-type=application/json"

print()
print(f"Server: {SERVER}")
print(f"URL: {SERVER + ENDPOINT + PARAMS}")

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}")

data = r1.read().decode("utf-8")
response = json.loads(data)
print()

termcolor.cprint("Gene: ", 'green', end="")
print("MIR633")

termcolor.cprint("Description: ", 'green', end="")
print(response['desc'])

termcolor.cprint("Bases: ", 'green', end="")
print(response['seq'])