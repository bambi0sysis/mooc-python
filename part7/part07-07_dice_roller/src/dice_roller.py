from random import choice

def roll(die: str):
    a = '333336'
    b = '222555'
    c = '144444'
    if die == 'A':
        return int(choice(a))
    elif die == 'B':
        return int(choice(b))
    else:
        return int(choice(c))

def play(die1: str, die2: str, times: int):
    d1 = d2 = tie = 0
    for _ in range(times):
        die1_output = roll(die1)
        die2_output = roll(die2)
        if die1_output == die2_output:
            tie += 1
        elif die1_output > die2_output:
            d1 += 1
        else:
            d2 += 1
    return d1, d2, tie