def older_people(people: list, year: int):
    old = []
    for p in people:
        if p[1] < year:
            old.append(p[0])
    return old