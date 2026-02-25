class Seq:

    def __init__(self, strbases = None):
        self.strbases = strbases
        bases = ["A", "G", "T", "C"]
        if strbases is None:
            self.strbases = "NulL"
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
        return len(self.strbases)
