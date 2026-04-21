from pathlib import Path

file = "sequences/RNU6_269P.txt"
contents = Path(file).read_text()
header = contents.split("\n")
changed1 = header[0]
print(f"First line of the RNU6_269P.txt file: {changed1}")