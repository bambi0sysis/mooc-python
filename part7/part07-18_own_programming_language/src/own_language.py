from string import ascii_uppercase


def operation(a, op, b):
    if op == "==":
        return a == b
    elif op == "!=":
        return a != b
    elif op == "<":
        return a < b
    elif op == "<=":
        return a <= b
    elif op == ">":
        return a > b
    elif op == ">=":
        return a >= b


def get_value(dictionary: dict, val):
    return dictionary[val] if val in ascii_uppercase else int(val)


def run(input_list: list):
    result = []

    variables = {}
    for value in ascii_uppercase:
        variables[value] = 0

    labels = {}
    for i in range(len(input_list)):
        if input_list[i][-1] == ":":
            labels[input_list[i][:-1]] = i

    i = 0
    while i < len(input_list):
        if input_list[i][:-1] not in labels:
            program = input_list[i].split()
            if program[0] == "PRINT":
                result.append(get_value(variables, program[-1]))
            elif program[0] == "MOV":
                variables[program[1]] = get_value(variables, program[-1])
            elif program[0] == "MUL":
                variables[program[1]] *= get_value(variables, program[-1])
            elif program[0] == "ADD":
                variables[program[1]] += get_value(variables, program[-1])
            elif program[0] == "SUB":
                variables[program[1]] -= get_value(variables, program[-1])
            elif program[0] == "JUMP":
                i = labels[program[-1]]
                continue
            elif program[0] == "IF":
                if operation(
                    get_value(variables, program[1]),
                    program[2],
                    get_value(variables, program[3]),
                ):
                    i = labels[program[-1]]
                    continue
                else:
                    pass
            elif program[0] == "END":
                break
        i += 1

    return result
