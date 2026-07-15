def recursive_sum(number: int):
    summ = number
    if number <= 1:
        return number
    summ += recursive_sum(number - 1)
    return summ
