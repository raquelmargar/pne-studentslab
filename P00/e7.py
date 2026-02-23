from Seq0 import seq_read_fasta, seq_complement

print("-----| Exercise 7 |------")

rute = "../S04/sequences/U5.txt"
g = seq_read_fasta(rute)

fragment = g[:20]

print("Gene U5:")
print("Frag:", fragment)
print("Comp:", seq_complement(fragment))