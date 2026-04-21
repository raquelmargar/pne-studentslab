from seq3 import seq_complement, seq_read_fasta

print(f"------| Exercise 6 |------")
adn = seq_read_fasta("../S04/sequences/U5.txt")
fragment = adn[:20]
comp = seq_complement(fragment)

print(f"Gene U5 \n Fragment: {fragment} \n Reverse: {comp}")