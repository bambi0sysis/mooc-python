from random import choice, shuffle, randint
from string import ascii_lowercase


def generate_strong_password(length: int, arg2: bool, arg3: bool):
    if length >= 3:
        num_of_nums = randint(1, length - 2)
    # print(num_of_nums)
    psswrd = []

    if arg2:
        nums = [str(n) for n in range(0, 10)]
        shuffle(nums)
        psswrd.extend(nums[:num_of_nums])

    if arg3:
        symbols = list("!?=+-()#")
        shuffle(symbols)
        psswrd.extend(symbols[: length - num_of_nums - 1])

    for i in range(length - len(psswrd)):
        psswrd.append(choice(ascii_lowercase))

    return "".join(psswrd)


# for i in range(10):
#     print(generate_strong_password(2, False, False))
