from Seq0 import seq_read_fasta, seq_reverse

rute = "../S04/sequences/U5.txt"
g = seq_read_fasta(rute)

print("------| Exercise 6 |------")
print("Gene U5")
print("Fragment: ", g[:20])
print("Reverse:  ", seq_reverse(g, 20)[:20])