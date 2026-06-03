def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in column:
            return False
        column.append(row[column_no])
    return True
