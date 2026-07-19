from random import choice


def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        yield "".join(choice(characters) for _ in range(length))


# def word_generator(characters: str, length: int, amount: int):
#     gen = ("".join(choice(characters) for _ in range(length)) for _ in range(amount))
#     return gen


# 1st version

# from random import sample


# # def word_generator(characters: str, length: int, amount: int):
# #     for _ in range(amount):
# #         yield "".join(sample(characters, length))


# def word_generator(characters: str, length: int, amount: int):
#     gen = ("".join(sample(characters, length)) for _ in range(amount))
#     return gen
