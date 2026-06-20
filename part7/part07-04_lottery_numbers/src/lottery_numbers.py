from random import sample


def lottery_numbers(amount: int, lower: int, upper: int):
    num = list(range(lower, upper + 1))
    l = sample(num, amount)
    return sorted(l)
