from seq3 import seq_count_base, seq_read_fasta

print(f"-----| Exercise 4 |------")
gene_list = ["U5", "ADA", "FRAT1",  "FXN"]
bases = ["A", "T", "G", "C"]

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    r = seq_read_fasta(rute)
    print(f"\n Gene: {gene}")

    for base in bases:
        num = seq_count_base(r, base)
        print(f"{base}: {num}")