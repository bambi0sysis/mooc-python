def row_correct(sudoku: list):
    for row in sudoku:
        check_row = []
        for item in row:
            if item > 0 and item in check_row:
                    return False
            check_row.append(item)
    return True  

def column_correct(sudoku: list):
    for i in range(0, 9):
        column = []
        for row in sudoku:    
            if row[i] > 0 and row[i] in column:
                return False
            column.append(row[i])
    return True

def block_correct(sudoku: list):
    # row_no = column_no = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # j = 0
            square = []
            for row in sudoku[i:i + 3]:
                for item in row[j:3 + j]:
                    if item > 0 and item in square:
                        return False
                    square.append(item)
    
        
    return True

def sudoku_grid_correct(sudoku: list):
    return row_correct(sudoku) and column_correct(sudoku) and block_correct(sudoku)

if __name__ == "__main__":
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2))