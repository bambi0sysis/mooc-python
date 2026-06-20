from fractions import Fraction
def fractionate(amount: int):
    return [Fraction(1, amount) for n in range(amount)]
