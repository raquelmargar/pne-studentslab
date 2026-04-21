from seq3 import seq_len, seq_read_fasta

gene_list = ["U5", "ADA", "FRAT1",  "FXN"]
print("-----| Exercise 3 |------")

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    r = seq_read_fasta(rute)
    l = seq_len(r)
    print(f"Gene {gene} -> Length: {l}")

