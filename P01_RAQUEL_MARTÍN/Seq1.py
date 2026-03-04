class Seq:

    def __init__(self, strbases = None):
        self.strbases = strbases
        bases = ["A", "G", "T", "C"]
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence Created")
            return
        else:
            base = True
            for i in self.strbases:
                if i in bases:
                    base = True
                else:
                    base = False
                    break
            if base:
                print("New sequence created!")
            else:
                print("INVALID sequence!")
                self.strbases = "ERROR"

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        else:
            bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

            for base in self.strbases:
                if base in bases:
                    bases[base] += 1

            return bases

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return "ERROR"
        else:
            reversed = self.strbases[::-1]
            return reversed

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return "ERROR"
        else:
            comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            new_seq = ""

            for base in self.strbases:
                new_seq += comp[base]

            return new_seq

    def read_fasta(self, filename):
        from pathlib import Path

        try:
            file_contents = Path(filename).read_text()
            text = file_contents.split("\n")[1:]
            final_text = "".join(text)

            for base in final_text:
                if base not in ["A", "T", "C", "G"]:
                    self.strbases = "ERROR"
                    print("INVALID sequence!")
                    return

            self.strbases = final_text
            print("New sequence loaded!")

        except FileNotFoundError:
            print(f"File {filename} not found")
            self.strbases = "ERROR"




