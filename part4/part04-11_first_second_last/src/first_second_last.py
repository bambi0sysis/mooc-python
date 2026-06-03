def find(string):
    pass


def first_word(string):
    i = string.find(" ")
    word = string[:i]
    return word

def second_word(string):
    i = string.find(" ")
    new = string[i + 1:]
    i = new.find(" ")
    if i == -1:
        return new
    word = new[:i]
    return word
    
def last_word(string):
    i = 0 
    l = len(string)
    while i < l:
        index = string.find(" ")
        string = string[index + 1:]
        i += 1
    return string

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word("first second"))
    print(last_word("please write a program which keeps asking the user for words"))



# def find(string, place):
#     i = 0
#     word = ""
#     counter = 0
#     while i < len(string):
#         if string[i] == " ":
#             counter += 1
#             if counter == place:
#                 break
#             word = ""
#         else:
#             word += string[i]
#         i += 1
#     return word

# def first_word(string):
#     return find(string, 1)

# def second_word(string):
#     return find(string, 2)

# def last_word(string):
#     return find(string, 0)

# if __name__ == "__main__":
#     sentence = "once upon a time there was a programmer"
#     print(first_word(sentence))
#     print(second_word("first second"))
#     print(last_word("please write a program which keeps asking the user for words"))



# def first_word(string):
#     word = string.find(" ")   
#     return string[: word]

# def second_word(Original_string):
#     word1 = Original_string.find(" ")
#     string = Original_string[word1 + 1:]
#     # print(word1)
#     # print(string)
#     word2 = string.find(" ")
#     # print(word2)
#     if word2 == -1:
#         return string
#     return string[: word2]

# def last_word(string):
#     l = len(string)
#     i = 0
#     while i < l:
#         word = string.find(" ")
#         string = string[word + 1:]
#         i += 1
#         # print(word, string, i, end = "\n")
#     return string

# if __name__ == "__main__":
#     sentence = "once upon a time there was a programmer"
#     print(first_word(sentence))
#     print(second_word("first second"))
#     print(last_word("please write a program which keeps asking the user for words"))