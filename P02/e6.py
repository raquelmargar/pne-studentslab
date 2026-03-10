from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "212.128.255.70"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

s = Seq()
gene = "FRAT1"
rute = "../S04/sequences/" + gene + ".txt"
base = str(s.read_fasta(rute))

print(f"Gene {gene}")
for i in range(0,10):

    l = base[10*i : 10*(i+1)]

    print(f"Fragment {i+1}: {l}")

    if (i+1) % 2 != 0:
        response = c1.talk(l)
    else:
        response = c2.talk(l)
    print(f"To server: {l}")
    print(f"From server: {response}")