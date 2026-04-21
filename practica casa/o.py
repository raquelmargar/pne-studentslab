seq = input("Introduce the sequence:")
print(f"Total length: {len(seq)}")

def count_bases(seq):
    bases = {"A": 0, "T": 0, "G": 0, "C": 0}

    for base in seq:
        bases[base] += 1

    return bases

counts = count_bases(seq)

for base in ["A", "G", "T", "C"]:
    print(f"{base}: {counts[base]}")