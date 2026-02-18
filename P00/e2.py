from Seq0 import seq_read_fasta

adn = seq_read_fasta("../S04/sequences/U5.txt")
print("DNA file: U5.txt")
print("The first 20 bases are:", adn[0:20])
