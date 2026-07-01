def calculate_result(person: dict):
    total = person["result1"] + person["result2"] + person["result3"]
    return total / 3


def smallest_average(person1: dict, person2: dict, person3: dict):
    results = {}

    results["person1"] = calculate_result(person1)
    results["person2"] = calculate_result(person2)
    results["person3"] = calculate_result(person3)

    minimum = results["person1"]
    minimum_name = "person1"
    for k, val in results.items():
        if val < minimum:
            minimum = val
            minimum_name = k

    if minimum_name == "person1":
        return person1
    elif minimum_name == "person2":
        return person2
    else:
        return person3
