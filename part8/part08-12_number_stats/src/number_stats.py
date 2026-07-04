class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number: int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers

    def average(self):
        if self.count != 0:
            return self.numbers / self.count
        return 0


num = NumberStats()
odd_num = NumberStats()
even_num = NumberStats()


while True:
    inpt = int(input("Please type in integer numbers: "))
    if inpt == -1:
        break
    num.add_number(inpt)
    if inpt % 2 == 0:
        even_num.add_number(inpt)
    else:
        odd_num.add_number(inpt)

print("Sum of numbers:", num.get_sum())
print("Mean of numbers:", num.average())
print("Sum of even numbers:", even_num.get_sum())
print("Sum of odd numbers:", odd_num.get_sum())
