from difflib import get_close_matches

sentence = input("write text: ").split()
result = []
incorrect = []

file_content = []

with open("wordlist.txt") as file:
    for word in file:
        file_content.append(word.strip())

for word in sentence:
    if word.lower() in file_content:
        result.append(word)
        continue
    result.append(f"*{word}*")
    incorrect.append(word)

print(" ".join(result))
print("suggestions:")

for word in incorrect:
    output = get_close_matches(word, file_content)
    print(f"{word}: {', '.join(output)}")
