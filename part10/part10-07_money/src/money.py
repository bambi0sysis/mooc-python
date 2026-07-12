class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another: "Money"):
        return (
            self.__euros * 100 + self.__cents == another.__euros * 100 + another.__cents
        )

    def __lt__(self, another: "Money"):
        return (
            self.__euros * 100 + self.__cents < another.__euros * 100 + another.__cents
        )

    def __gt__(self, another: "Money"):
        return (
            self.__euros * 100 + self.__cents > another.__euros * 100 + another.__cents
        )

    def __ne__(self, another: "Money"):
        return (
            self.__euros * 100 + self.__cents != another.__euros * 100 + another.__cents
        )

    def __add__(self, another: "Money"):
        selfs = self.__euros * 100 + self.__cents
        anothers = another.__euros * 100 + another.__cents
        euros = (selfs + anothers) // 100
        cents = (selfs + anothers) % 100
        return Money(euros, cents)

    def __sub__(self, another: "Money"):
        selfs = self.__euros * 100 + self.__cents
        anothers = another.__euros * 100 + another.__cents
        diff = selfs - anothers
        euros = diff // 100
        cents = abs(diff % 100)
        if self.__euros == another.__euros and self.__cents < another.__cents:
            raise ValueError("negative sub not allowed")
        if diff < 0 and cents != 0:
            euros -= 1
            cents = 100 - cents
        if diff < 0 and cents == 0:
            raise ValueError("negative sub not allowed")
        return Money(euros, cents)
