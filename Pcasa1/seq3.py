from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    seq_contents = Path(filename).read_text()
    contents = seq_contents.split("\n")[1:]
    final_contents = "".join(contents)
    return final_contents

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    bases = {"A": 0, "T": 0, "G": 0, "C": 0}

    for base in seq:
        bases[base] += 1

    return bases

def seq_reverse(seq, n):
    cut = seq[:n]
    reversd = cut[::-1]

    return reversd

def seq_complement(seq):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    n_seq = ""

    for base in seq:
        n_seq += comp[base]

    return n_seq

