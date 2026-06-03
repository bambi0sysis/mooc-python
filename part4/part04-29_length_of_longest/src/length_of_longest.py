def length_of_longest(l: list):
    length = 0
    for string in l:
        if len(string) > length:
            length = len(string)
    return length