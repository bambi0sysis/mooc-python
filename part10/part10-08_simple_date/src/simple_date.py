class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = [date, month, year]

    def __gt__(self, another: "SimpleDate"):
        if self.__date[2] > another.__date[2]:
            return True
        elif self.__date[2] < another.__date[2]:
            return False
        else:
            if self.__date[1] > another.__date[1]:
                return True
            elif self.__date[1] < another.__date[1]:
                return False
            else:
                if self.__date[0] > another.__date[0]:
                    return True
                else:
                    return False

    def __lt__(self, another: "SimpleDate"):
        if self.__date[2] < another.__date[2]:
            return True
        elif self.__date[2] > another.__date[2]:
            return False
        else:
            if self.__date[1] < another.__date[1]:
                return True
            elif self.__date[1] > another.__date[1]:
                return False
            else:
                if self.__date[0] < another.__date[0]:
                    return True
                else:
                    return False

    def __eq__(self, another: "SimpleDate"):
        return self.__date == another.__date

    def __ne__(self, another: "SimpleDate"):
        return self.__date != another.__date

    def __str__(self):
        return f"{self.__date[0]}.{self.__date[1]}.{self.__date[2]}"

    def __add__(self, days: int):
        new = SimpleDate(self.__date[0], self.__date[1], self.__date[2])
        if new.__date[0] + days <= 30:
            new.__date[0] += days
        else:
            while days >= 360:
                new.__date[2] += 1
                days -= 360
            new.__date[0] = new.__date[0] + days
        while new.__date[0] > 30:
            new.__date[0] -= 30
            new.__date[1] += 1
            if new.__date[1] > 12:
                new.__date[2] += 1
                new.__date[1] = new.__date[1] - 12
        return new

    def __sub__(self, another: "SimpleDate"):
        years = self.__date[2] - another.__date[2]
        months = self.__date[1] - another.__date[1]
        days = self.__date[0] - another.__date[0]
        if years < 0:
            months = another.__date[1] - self.__date[1]
            days = another.__date[0] - self.__date[0]
            years = abs(years)
        if months < 0:
            months += 12
            years -= 1
        if days < 0:
            days += 30
            months -= 1

        return abs(days + 30 * months + 360 * years)
