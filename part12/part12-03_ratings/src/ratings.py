def sort_by_ratings(items: list):
    def rating(d: dict):
        return d["rating"]

    return sorted(items, key=rating, reverse=True)
