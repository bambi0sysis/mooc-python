def new_person(name: str, age: int):
    if len(name.split()) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError
    return name, age

# print(new_person('Andrew', 32))