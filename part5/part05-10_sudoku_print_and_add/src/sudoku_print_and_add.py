def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                print("_", end = " ")
            else:
                print(sudoku[i][j], end = " ")
            if j % 3 == 2 and j < 8:
                print(end = " ")
        print()
        if i % 3 == 2 and i < 8:
            print()

# def print_sudoku(sudoku: list):
#     for i in range(len(sudoku)):
#         for j in range(len(sudoku[i])):
#             if sudoku[i][j] == 0:
#                 print("_", end = " ")
#             else:
#                 print(sudoku[i][j], end = " ")
#             if j % 3 == 2:
#                 print(end= " ")
#         print()
#         if i % 3 == 2:
#             print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number