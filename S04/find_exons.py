from pathlib import Path

FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()
a = file_contents.split("\n")
body = a[1::]
b = "".join(body)

exon = b.find("GCTGGCCCCAGGGAAAGCCGAGCGGCCACCGAGCCGGCAGAGACCCACCGAGCGGCGGCGGAGGGAGCAGCGCCGGGGCGCACGAGGGCACCATGGCCCAGACGCCCGCCTTCGACAAGCCCAAA")
print(exon)