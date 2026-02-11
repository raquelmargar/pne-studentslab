from dna_count import count_bases

#option 1
f = open("dan.txt","r")
lines = f.readlines()
f.close()

#option 2
with open("dna.txt","r") as f:
    linesz = f.readlines()

count_bases("")