from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.70" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

s = Seq()
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"

    s.read_fasta(rute)

    print(f"Sending the {gene} to the server...")
    response = c.talk(str(s))
    print(f"To server: {str(s)}")

    print(f"From server: {response}")
