class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]


def total_units(my_list: ShoppingList):
    units = 0
    for i in range(my_list.number_of_items()):
        units += my_list.amount(i)
    return units
