def filter_solutions():
    correct = []
    incorrect = []
    with open('solutions.csv') as file:
        for ls in file:
            ls = ls.strip().split(';')
            if '+' in ls[1]:
                op = ls[1].split('+')
                op = [int(o) for o in op]
                if op[0] + op[1] == int(ls[2]):
                    correct.append(ls)
                else:
                    incorrect.append(ls)
            elif '-' in ls[1]:
                op = ls[1].split('-')
                op = [int(o) for o in op]
                if op[0] - op[1] == int(ls[2]):
                    correct.append(ls)
                else:
                    incorrect.append(ls)

    with open('correct.csv', "w") as file:
        for lst in correct:
            row = ';'.join(lst)
            file.write(row + '\n')

    with open('incorrect.csv', "w") as file:
        for lst in incorrect:
            r = ';'.join(lst)
            file.write(r + '\n')

# correct = []
# incorrect = []
# ls = 'Pekka;3-2;1'.strip().split(';')
# if '+' in ls[1]:
#     index = ls[1].find('+')
#     op1 = int(ls[1][:index]) 
#     op2 = int(ls[1][index + 1:])
#     if op1 + op2 == int(ls[2]):
#         correct.append(ls)
#     else:
#         incorrect.append(ls)
# elif '-' in ls[1]:
#     index = ls[1].find('-')
#     op1 = int(ls[1][:index]) 
#     op2 = int(ls[1][index + 1:])
#     if op1 - op2 == int(ls[2]):
#         correct.append(ls)
#     else:
#         incorrect.append(ls)
# print(correct, incorrect)

# if '+' in ls[1]:
#     op = ls[1].split('+')
#     op = [int(o) for o in op]
#     if op[0] + op[1] == int(ls[2]):
#         correct.append(ls)
#     else:
#         incorrect.append(ls)
# elif '-' in ls[1]:
#     op = ls[1].split('-')
#     op = [int(o) for o in op]
#     if op[0] - op[1] == int(ls[2]):
#         correct.append(ls)
#     else:
#         incorrect.append(ls)

# # op1 = int(ls[1][0])
# # op = ls[1][1]
# # op2 = int(ls[1][2])
# if op == '+':
#     if op1 + op2 == int(ls[2]):
#         correct.append(ls)
#     else:
#         incorrect.append(ls)
# elif op == "-":
#     if op1 - op2 == int(ls[2]):
#         correct.append(ls)
#     else:
#         incorrect.append(ls)
# print(correct, incorrect)

# for lst in correct:
#     row = str(lst)[1:-1].replace(",", ";").replace(" ", "")
# print(row)