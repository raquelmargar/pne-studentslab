from o import count_bases

with open("dna.txt", "r") as t:
    lines = t.readlines()
for i in lines:
    seq = i.strip()
    print(f"{count_bases(seq)}")
    print(f"Total length: {len(seq)}")