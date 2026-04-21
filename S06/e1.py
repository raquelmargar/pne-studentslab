class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        bases = ["A", "G", "T", "C"]
        base = True
        for i in self.strbases:
            if i not in bases:
                base = False
                break  # salimos en cuanto hay error

        if base:
            print("New sequence created!")
        else:
            print("INCORRECT Sequence detected")
            self.strbases = "ERROR!"

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
