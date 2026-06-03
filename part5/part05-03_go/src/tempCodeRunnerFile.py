def who_won(game_board: list):

    # for row in game_board:
    #     for square in row:
    if game_board.count(1) > game_board.count(2):
        return 1
    elif game_board.count(2) > game_board.count(1):
        return 2
    else:
        return 0

    print(game_board.count(0))