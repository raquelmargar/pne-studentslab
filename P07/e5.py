from P01_RAQUEL_MARTÍN.Seq1 import Seq
import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
genes = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6-269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}

for gene, gene_id in genes.items():
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", f"/sequence/id/{gene_id}?content-type=application/json")

    r1 = conn.getresponse()
    data = r1.read().decode("utf-8")
    response = json.loads(data)

    seq_str = response['seq']
    sequence = Seq(seq_str)

    counts = sequence.count()
    total = sequence.len()

    print()

    termcolor.cprint("Gene: ", "green", end="")
    print(gene)

    termcolor.cprint("Description: ", "green", end="")
    print(response['desc'])

    print("New sequence created!")

    termcolor.cprint("Total length: ", "green", end="")
    print(total)

    for base in ["A", "T", "C", "G"]:
        percentage = round((counts[base] / total) * 100, 1)
        termcolor.cprint(base + ":", "blue", end="")
        print(f" {counts[base]} ({percentage}%)")

    termcolor.cprint("Most frequent base: ", "green", end="")
    print(max(counts, key=counts.get))