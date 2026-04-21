from seq3 import seq_count, seq_read_fasta

print(f"-----| Exercise 5 |------")
gene_list = ["U5", "ADA", "FRAT1",  "FXN"]

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    r = seq_read_fasta(rute)
    c = seq_count(r)
    print(f"Gene{gene}: {c}")
