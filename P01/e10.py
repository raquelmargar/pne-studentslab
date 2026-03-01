from Seq1 import Seq

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Practice 1, Exercise 10 |------")

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"

    s = Seq()
    s.read_fasta(rute)

    counts = s.count()
    most_frequent = max(counts, key=counts.get)

    print(f"Gene {gene}: Most frequent Base: {most_frequent}")