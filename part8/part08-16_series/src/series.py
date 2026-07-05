class Series:
    def __init__(self, name: str, seasons: int, genres: list):
        self.title = name
        self.seasons = seasons
        self.genres = genres
        self.review = 0
        self.count = 0

    def rate(self, rating: int):
        self.review += rating
        self.count += 1

    def __str__(self):
        avg = self.review / self.count if self.count > 0 else self.review
        genre = ", ".join(self.genres)
        if self.review > 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre}\n{self.count} ratings, average {avg:.1f} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre}\nno ratings"


def minimum_grade(rating: float, series_list: list):
    result = []
    for person in series_list:
        review = person.review / person.count if person.count > 0 else person.review
        if review >= rating:
            result.append(person)
    return result


def includes_genre(genre: str, series_list: list):
    result = []
    for person in series_list:
        if genre in person.genres:
            result.append(person)
    return result
