# second try to make it better. is it better? i wonder!
def is_valid_line(line: str) -> bool:
    line = line.split(";")
    header = line[0]
    data = line[1].split(",")

    try:
        header_num = int(header.split(" ")[1])
        if len(data) != 7:
            return False
        data = [int(n) for n in line[1].split(",")]
        if max(data) > 39 or min(data) < 1:
            return False
        if len(set(data)) != len(data):
            return False
        return True

    except ValueError:
        return False


def filter_incorrect():
    with (
        open("lottery_numbers.csv") as file,
        open("correct_numbers.csv", "w") as w_file,
    ):
        for line in file:
            if is_valid_line(line):
                w_file.write(line)


# first try that passed the tmc
# def read_file():
#     file_lst = []
#     with open('lottery_numbers.csv') as file:
#         for line in file:
#             line = line.split(',')
#             line = line[0].split(';') + line[1:]
#             file_lst.append(tuple(line))
#     return file_lst

# def filter_incorrect():
#     context = read_file()
#     with open('correct_numbers.csv', 'w') as file:
#         for week in context:
#             check = True
#             if len(week) != 8:
#                 check = False
#             if len(set(week)) != len(week):
#                 check = False
#             try:
#                 int(week[0].split()[1])
#                 for num in week[1:]:
#                     int(num)
#                 for num in week[1:]:
#                     if int(num) < 1 or int(num) > 39:
#                         check = False
#                         break
#             except ValueError:
#                 check = False

#             if check:
#                 file.write(f'{week[0]};' + ','.join(week[1:]))
