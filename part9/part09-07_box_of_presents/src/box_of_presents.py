class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self):
        self.box = []

    def add_present(self, present: Present):
        self.box.append(present)

    def total_weight(self):
        combined_weight = 0
        for gift in self.box:
            combined_weight += gift.weight
        return combined_weight
