def even_numbers(l: list):
    l2 = []
    for i in l:
        if i % 2 == 0:
            l2.append(i)
    return l2