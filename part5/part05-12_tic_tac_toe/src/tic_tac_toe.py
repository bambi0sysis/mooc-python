def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 <= y < len(game_board) and 0 <= x < len(game_board[y]) and not game_board[y][x]:
        game_board[y][x] = piece
        return True
    return False