class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        height = 0
        for person in self.persons:
            height += person.height
        print(
            f"There are {len(self.persons)} persons in the room, and their combined height is {height} cm"
        )
        for person in self.persons:
            print(person)

    def shortest(self):
        if not self.persons:
            return None
        shortest_person = self.persons[0]
        height = self.persons[0].height
        for person in self.persons:
            if person.height < height:
                height = person.height
                shortest_person = person
        return shortest_person

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)

        return shortest_person
