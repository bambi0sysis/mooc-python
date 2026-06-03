def remove_smallest(numbers: list):
    cpy = numbers[0]
    for i in numbers:
        if i < cpy:
            cpy = i
    numbers.remove(cpy)
