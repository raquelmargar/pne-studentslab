from seq3 import seq_reverse, seq_read_fasta

print(f"------| Exercise 6 |------")
adn = seq_read_fasta("../S04/sequences/U5.txt")
reverse = seq_reverse(adn, 20)

print(f"Gene U5 \n Fragment: {adn[0:20]} \n Reverse: {reverse}")