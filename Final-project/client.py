# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

final_data = json.loads(data1)
print(f"CONTENT: {final_data}")