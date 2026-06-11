inpt_l = input("Write text: ")
inpt = inpt_l.split()

wordlst = set()
with open('wordlist.txt') as file:
    for line in file:
        wordlst.add(line.strip().lower())

output = []
for word in inpt:
    if word.lower() in wordlst:
        output.append(word)
    else:
        output.append(f"*{word}*")

i = 0
while i < len(output) - 1:
    print(output[i], end = " ")
    i += 1
print(output[-1])