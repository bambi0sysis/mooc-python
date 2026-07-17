def sort_by_remaining_stock(items: list):
    def remaining_stock(t: tuple):
        return t[-1]

    return sorted(items, key=remaining_stock)
