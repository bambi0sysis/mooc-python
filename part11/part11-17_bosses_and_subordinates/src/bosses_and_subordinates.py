class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: "Employee"):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    if len(employee.subordinates) == 0:
        return 0
    count = len(employee.subordinates)
    for member in employee.subordinates:
        count += count_subordinates(member)
    return count
