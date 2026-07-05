from datetime import datetime, timedelta


class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.date = datetime(2000, 1, 1, 0, self.minutes, self.seconds)

    def tick(self):
        self.date += timedelta(seconds=1)

    def __str__(self):
        minute = f"0{self.date.minute}" if self.date.minute <= 9 else self.date.minute
        second = f"0{self.date.second}" if self.date.second <= 9 else self.date.second
        return f"{minute}:{second}"
