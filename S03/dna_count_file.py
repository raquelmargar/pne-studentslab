#option 1
f = open("dan.txt","r")
lines = f.readlines()
f.close()

#option 2
with open("dna.txt","r") as f:
    lines = f.readlines()

def length_dna(sequence):
    return len(sequence)

def count_bases(sequence):
    count_A = count_C = count_T = count_G = 0
    for i in sequence:
        if i == "A":
            count_A += 1
        elif i == "C":
            count_C += 1
        elif i == "T":
            count_T += 1
        else:
            count_G += 1
    return(count_A, count_C, count_T, count_G)

sequence = input("Enter a DNA sequence: ")
length = length_dna(sequence)
a, c, t, g = count_bases(sequence)

print("Total length: ", length)
print("A: ", a)
print("C: ", c)
print("T: ", t)
print("G: ", g)

