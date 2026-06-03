def no_vowels(string: str):
    vowels = "aeiou"
    result = ""
    for ch in string:
        if ch not in vowels:
            result += ch
    return result


# def no_vowels(string: str):
#     vowels = "aeiou"
#     new_string = string
#     for ch in vowels:
#         new_string = new_string.replace(ch, "")
#     return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))