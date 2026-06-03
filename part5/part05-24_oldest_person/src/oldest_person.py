def oldest_person(people: list):
    min = people[0]
    for t in people:
        if t[1] < min[1]:
            min = t
    return min[0]