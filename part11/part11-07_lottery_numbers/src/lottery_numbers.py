class LotteryNumbers:
    def __init__(self, week_no: int, lottery_numbers: list):
        self.__week_no = week_no
        self.__lottery_numbers = lottery_numbers

    def number_of_hits(self, numbers: list):
        return len([num for num in numbers if num in self.__lottery_numbers])

    def hits_in_place(self, numbers: list):
        return [num if num in self.__lottery_numbers else -1 for num in numbers]
