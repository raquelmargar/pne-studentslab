from Seq0 import seq_len, seq_read_fasta

gene_list = ["U5", "ADA", "FRAT1",  "FXN"]
print("-----| Exercise 3 |------")
for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    g = seq_read_fasta(rute)
    print(gene, "-> Lenght:", seq_len(g))


