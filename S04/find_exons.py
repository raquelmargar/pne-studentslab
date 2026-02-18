from pathlib import Path

FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()
a = file_contents.split("\n")
body = a[1::]
gene_seq = "".join(body)

MAX_COORD = 44652852
EXON_FILE = "sequences/ADA_EXONS.txt"
exon_contents = Path(EXON_FILE).read_text()
exons = exon_contents.split(">")
#tienes que separar cada exon con > y luego quitarle esa primera linea,que es el header
print("Exon     | Long.  | Start            | End")
print("-----------------------------------------------------")

n = 1

for exon in exons:
    index = gene_seq.find(exon)
    length = len(exon)

    huge_coord = MAX_COORD - index
    little_coord = MAX_COORD - (index + length - 1)

    print(n, " | ", length, " | ", little_coord, " | ", huge_coord)
    n += 1