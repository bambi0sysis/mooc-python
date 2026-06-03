layers = int(input("Layers: "))
size = 2 * layers - 1
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for r in range(size):
    for c in range(size):
        bottom = size - 1 - r
        right = size - 1 - c
        
        distance = min(r, c, bottom, right)
        letter_index = layers - 1 - distance
        print(alphabets[letter_index], end = "")
    print()