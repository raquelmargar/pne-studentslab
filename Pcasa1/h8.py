from seq3 import seq_read_fasta, seq_count

print(f"-----| Exercise 8 |------")

gene_list = ["U5", "ADA", "FRAT1",  "FXN"]

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    r = seq_read_fasta(rute)

    maxims = seq_count(r)

    z = max(maxims, key=maxims.get)
    print(f"Gene {gene} Most frequent Base: {z}")
