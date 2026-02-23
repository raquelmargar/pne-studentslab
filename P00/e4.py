from Seq0 import seq_count_base, seq_read_fasta

gene_list = ["U5", "ADA", "FRAT1",  "FXN"]
bases = ["A", "T", "G", "C"]

print("-----| Exercise 4 |------")
for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    g = seq_read_fasta(rute)
    print(f"\nGene {gene}:")
    for b in bases:
        n = seq_count_base(g, b)
        print(f"{b}: {n}")