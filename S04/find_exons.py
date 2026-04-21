from pathlib import Path
from process_exons import get_exons_from_file

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")
body = lines[1:]
gene_seq = "".join(body)

MAX_COORD = 44652852
EXON_FILE = "sequences/ADA_EXONS.txt"
exon_contents = Path(EXON_FILE).read_text()

exons = get_exons_from_file(exon_contents)

print("Exon     | Long.  | Start            | End")
print("-----------------------------------------------------")

n = 1
for exon in exons:
    index = gene_seq.find(exon)
    length = len(exon)
    huge_coord = MAX_COORD - index
    little_coord = MAX_COORD - (index + length - 1)
    print(f"{n}| {length}| {little_coord}| {huge_coord}")
    n += 1