from Seq0 import seq_read_fasta, seq_count

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 5 |------")

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    g = seq_read_fasta(rute)
    d = seq_count(g)

    print(f"Gene {gene}: {d}")