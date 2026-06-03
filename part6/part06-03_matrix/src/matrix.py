def matrix_sum():
    with open('matrix.txt') as file:
        summ = 0
        for line in file:
            line = line.strip()
            lst = line.split(',')
            for i in lst:
                summ += int(i)
    return summ

def matrix_max():
    with open('matrix.txt') as file:
        start = True
        maxm = 0
        for line in file:
            line = line.strip()
            lst = line.split(',')
            for i in lst:
                if start or int(i) > maxm:
                    maxm = int(i)
                    start = False
    return maxm

def row_sums():
    with open('matrix.txt') as file:
        row = []
        for line in file:
            line = line.strip()
            row.append(sum([int(val) for val in line.split(',')]))
    return row

# def common(filename: str):
#     with open('matrix.txt') as file:
#         row = []
#         for line in file:
#             line = line.strip()