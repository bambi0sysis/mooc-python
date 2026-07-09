class ListHelper:
    def __init__(self, lst: list):
        self.lst = lst

    @classmethod
    def greatest_frequency(cls, my_list: list):
        if my_list:
            most_common = my_list[0]
        highest_count = 0
        for item in my_list:
            if my_list.count(item) > highest_count:
                most_common = item
                highest_count = my_list.count(item)
        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        doubles_my_list = []
        for item in my_list:
            if my_list.count(item) > 1:
                if item not in doubles_my_list:
                    doubles_my_list.append(item)
        return len(doubles_my_list)
