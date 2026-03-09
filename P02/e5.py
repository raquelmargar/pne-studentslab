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
base = str(s.read_fasta(rute))

print(f"Gene {gene}")
for i in range(0, 5):

    l = base[10*i : 10*(i+1)]
    print(f"Fragment {i+1}: {l}")
    response = c.talk(l)

    print(f"To server: {l}")
    print(f"From server: {response}")