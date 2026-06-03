def who_won(game_board: list):
    # count1 = [] 
    points1 = 0
    points2 = 0
    # count2 = []
    for row in game_board:
        for square in row:
            if square == 1:
                # count1.append(square)
                points1 += 1
            elif square == 2:
                # count2.append(square)
                points2 += 1
    # if len(count1) > len(count2):
    if points1 > points2:
        return 1
    # elif len(count2) > len(count1):
    elif points1 < points2:
        return 2
    else:
        return 0
# rather than using lists,
# use variable to check it