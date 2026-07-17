def sort_by_seasons(items: list):
    def season(d: dict):
        return d["seasons"]

    return sorted(items, key=season)
