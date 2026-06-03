def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy = sudoku[:]
    for i in range(len(copy)):
        copy[i] = sudoku[i][:]
    # copy = []
    # for r in sudoku:
    #    copy.append(r[:])
    copy[row_no][column_no] = number
    return copy

# learn to copy from the model solution
# n = []
# for r in sudoku:
#     n.append(r[:])