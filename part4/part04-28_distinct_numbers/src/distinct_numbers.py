def distinct_numbers(l: list):
    distinct = []
    for i in l:
        if i not in distinct:
            distinct.append(i)
    # return sorted(distinct)
    return distinct.sort()
# dont create extra dup no?