def read_input(st: str, lower_limit: int, upper_limit: int):
    while True:
        try:
            num = int(input(st))
            if lower_limit < num < upper_limit:
                return num
        except ValueError:
            pass
        print(f'You must type in an integer between {lower_limit} and {upper_limit}')

# number = read_input("Please type in a number: ", 1, 5)
# print("You typed in:", number)