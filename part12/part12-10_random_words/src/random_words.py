from random import sample


# def word_generator(characters: str, length: int, amount: int):
#     for _ in range(amount):
#         yield "".join(sample(characters, length))


def word_generator(characters: str, length: int, amount: int):
    gen = ("".join(sample(characters, length)) for _ in range(amount))
    return gen
