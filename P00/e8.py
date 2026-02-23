from Seq0 import seq_read_fasta, seq_count

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 8 |------")

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    g = seq_read_fasta(rute)

    counts = seq_count(g)

    most_frequent = max(counts, key=counts.get)

    print(f"Gene {gene}: Most frequent Base: {most_frequent}")