class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


def fastest_car(cars: list):
    make = ""
    top = 0
    for car in cars:
        if car.top_speed > top:
            make = car.make
            top = car.top_speed
    return make
