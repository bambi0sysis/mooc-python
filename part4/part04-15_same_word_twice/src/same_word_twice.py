l = []
while True:
    word = input("Word: ")
    if word not in l:
        l.append(word)
        continue
    break
print(f"You typed in {len(l)} different words")