import json

def print_persons(filename: str):

    with open(filename) as file:
        data = file.read()

    data_in_py = json.loads(data)

    for dictionary in data_in_py:
        print(f'{dictionary['name']} {dictionary['age']} years (', end = "")
        if dictionary['hobbies']:
            for hobby in dictionary['hobbies'][:-1]:
                print(f'{hobby}, ', end = "")
            print(f'{dictionary['hobbies'][-1]})')
        else:
            print(')')