def everything_reversed(l: list):
    # l = l[::-1]
    l2 = []
    for string in l:
        l2.append(string[::-1])
    # return l2
    return l2[::-1]