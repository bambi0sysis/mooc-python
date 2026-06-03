def block_correct(sudoku: list, row_no: int, column_no: int):
    square = []
    for row in sudoku[row_no: row_no + 3]:
        for item in row[column_no: column_no +3]:
            if item > 0 and item in square:
                return False
            square.append(item)
    return True
