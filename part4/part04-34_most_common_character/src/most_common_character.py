def most_common_character(string: str):
    # winner = ""
    winner = string[0]
    for ch in string:
        if string.count(ch) > string.count(winner):
            winner = ch
    return winner

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
