class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def weight(self):
        return self.__weight

    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcase = []

    def add_item(self, g_item: Item):
        if g_item.weight() + self.weight() <= self.__max_weight:
            self.__suitcase.append(g_item)

    def __str__(self):
        if len(self.__suitcase) == 1:
            return f"{len(self.__suitcase)} item ({self.weight()} kg)"
        return f"{len(self.__suitcase)} items ({self.weight()} kg)"

    def print_items(self):
        for item in self.__suitcase:
            print(item)

    def weight(self):
        weight_sum = 0
        for item in self.__suitcase:
            weight_sum += item.weight()
        return weight_sum

    def heaviest_item(self):
        if not self.__suitcase:
            return None
        heaviest_item = self.__suitcase[0]
        for item in self.__suitcase:
            if item.weight() > heaviest_item.weight():
                heaviest_item = item
        return heaviest_item


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__cargo = []

    def add_suitcase(self, suitcase: Suitcase):
        current_weight = 0
        for scase in self.__cargo:
            current_weight += scase.weight()
        if suitcase.weight() + current_weight <= self.__max_weight:
            self.__cargo.append(suitcase)

    def __str__(self):
        weight = 0
        for scase in self.__cargo:
            weight += scase.weight()
        if len(self.__cargo) == 1:
            return f"{len(self.__cargo)} suitcase, space for {self.__max_weight - weight} kg"
        return (
            f"{len(self.__cargo)} suitcases, space for {self.__max_weight - weight} kg"
        )

    def print_items(self):
        for scase in self.__cargo:
            scase.print_items()
