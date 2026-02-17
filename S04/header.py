from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

a = file_contents.split("\n")
header = a[0]
print("First line of the RNU6_269P.txt file:", header)