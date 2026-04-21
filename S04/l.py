from pathlib import Path

file = "sequences/ADA_EXONS.txt"
filename = Path(file).read_text()

def get_exons_from_file(filename):
    list1 = []
    exons = filename.split(">")
    for exon in exons:
        if exon != "":
            new_exon = exon.split("\n")
            wo_hea = new_exon[1:]
            clean = "".join(wo_hea)
            list1.append(clean)
    return list1

print(f"The ADA_EXONS.txt clean is: {get_exons_from_file(filename)}")