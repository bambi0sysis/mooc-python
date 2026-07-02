def list_years(dates: list):
    lst = []
    for day in dates:
        lst.append(day.year)
    lst.sort()
    return lst
