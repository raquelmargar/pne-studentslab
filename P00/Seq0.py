from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    text = file_contents.split("\n")[1::]
    final_text = "".join(text)
    return final_text

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    d = {'A':0, 'T':0, 'C':0, 'G':0}

    for base in seq:
        if base in d:
            d[base] += 1

    return d