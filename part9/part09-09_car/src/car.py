class Car:
    def __init__(self):
        self.__petrol_amount = 0
        self.__reading = 0

    def fill_up(self):
        self.__petrol_amount = 60

    def drive(self, km: int):
        if self.__petrol_amount - km >= 0:
            self.__petrol_amount -= km
            self.__reading += km
        else:
            self.__reading += self.__petrol_amount
            self.__petrol_amount = 0

    def __str__(self):
        return f"Car: odometer reading {self.__reading} km, petrol remaining {self.__petrol_amount} litres"
