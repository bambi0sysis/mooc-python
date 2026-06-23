from random import sample

def words(n: int, beginning: str):
    result = []
    with open('words.txt') as file:
        for row in file:
            row = row.strip()
            if row.startswith(beginning) and row not in result:
                result.append(row)
    if len(result) < n:
        raise ValueError('Not enough words beginning with the specified string!')
    return sample(result, n)
