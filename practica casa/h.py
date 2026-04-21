from pithlab import path

file = "RNU6_269P.txt"
contents = path(file).read_text()
header = contents.split("\n")
changed1 = HEADER[0]
print(f"First line of the RNU6_269P.txt file: {changed1}")