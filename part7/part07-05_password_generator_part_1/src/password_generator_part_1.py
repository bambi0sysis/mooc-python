import string
import random


def generate_password(length: int):
    psswrd = ""
    for _ in range(length):
        psswrd += random.choice(string.ascii_lowercase)
    return psswrd
