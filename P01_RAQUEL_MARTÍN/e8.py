from Seq1 import Seq

print("-----| Practice 1, Exercise 8 |------")
sequences = [Seq(), Seq("ACTGA"), Seq("ATGHFT")]

for i, seq in enumerate(sequences): #enumerate es una función que usas para que te salga lo de seq1, se2 porque sino te saldría pero sin el indice
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
    print(f"  Bases: {seq.count()}")
    print(f"  Rev:   {seq.reverse()}")
    print(f"  Comp:  {seq.complement()}")