from pathlib import Path

file = "sequences/U5.txt"
contents = Path(file).read_text()

clean = contents.split("\n")
body = clean[1:]
new_body = "".join(body)
print(f"Body of the U5.txt file: \n {new_body}")
