def no_shouting(l: list):
    l2 = []
    for string in l:
        if not string.isupper():
            l2.append(string)
    return l2