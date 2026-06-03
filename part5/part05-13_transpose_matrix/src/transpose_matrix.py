def transpose(matrix: list):
    transposed = []
    for r in matrix:
        transposed.append(r[:])
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[c][r] = transposed[r][c]
# works but is wrong as it may show errors and im re-writing,
# or assigning, which wasnt what was asked, they asked me to
# transpose, not create a new_list and do stuff..
# THIS IS MANIPULATION, NOT THE CORRECT ANSWER!!!

def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and i < j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                # print(matrix[i][j])
                # print(matrix[j][i])

# max = [[1,2,3],[4,5,6],[7,8,9]]
# transpose(max)
# print(max)

# 1 2 3
# 4 5 6
# 7 8 9

def transpose(matrix: list):
    for r in range(len(matrix)):
        for c in range(r, len(matrix)):
            temp = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = temp