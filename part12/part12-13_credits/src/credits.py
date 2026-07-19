from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(attempts: list):
    return reduce(lambda summ, x: summ + x.credits, attempts, 0)


def sum_of_passed_credits(attempts: list):
    attempts_filtered = filter(lambda x: x.grade > 0, attempts)
    return reduce(lambda summ, x: summ + x.credits, attempts_filtered, 0)


def average(attempts: list):
    attempts_filtered = list(filter(lambda x: x.grade > 0, attempts))
    return reduce(lambda summ, x: summ + x.grade, attempts_filtered, 0) / len(
        attempts_filtered
    )
