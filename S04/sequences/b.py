from pathlib import Path

file = "ADA.txt"
contents = Path(file).read_text()

clean = contents.split("\n")
body = clean[1:]
new_body = "".join(body)
print(f"Body of the U5.txt file: {len(new_body)}")