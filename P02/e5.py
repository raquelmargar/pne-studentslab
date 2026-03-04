from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.70" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

s = Seq()
gene = "FRAT1"
rute = "../S04/sequences/" + gene + ".txt"
base = s.read_fasta(rute)

for i in range(0, 5):
    l = base[10 * i : 10]



    print(f"Sending the {gene} to the server...")
    response = c.talk(str(s))
    print(f"To server: {str(s)}")

    print(f"From server: {response}")
