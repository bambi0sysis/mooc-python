def palindromes(string: str):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True
while True:
    word = input("Please type in  a palindrome: ")
    if palindromes(word):
        print(word, "is a palindrome!")
        break
    print("that wasn't a palindrome")