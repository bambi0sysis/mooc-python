class CourseRecords:
    def __init__(self):
        self.__courses = {}
        self.__credits = 0
        self.__grades = [0, 0, 0, 0, 0, 0]

    def add_course(self, course: str, grade: int, credits: int):
        if course not in self.__courses:
            self.__courses[course] = (grade, credits)
        elif grade > self.__courses[course][0]:
            self.__courses[course] = (grade, credits)

    def __helper(self):
        self.__credits = 0
        self.__grades = [0] * 6
        for course in self.__courses:
            self.__grades[self.__courses[course][0]] += 1
            self.__credits += self.__courses[course][1]

    def get_course_data(self, course: str):
        if course in self.__courses:
            return self.__courses[course]
        return None

    def __mean_grade(self):
        if not self.__grades:
            return 0
        summ = 0
        for grade in range(len(self.__grades)):
            summ += self.__grades[grade] * grade

        return f"{summ / len(self.__courses):.1f}"

    def stats(self):
        self.__helper()
        print(
            f"{len(self.__courses)} completed courses, a total of {self.__credits} credits"
        )
        mean = self.__mean_grade()
        print(f"mean {mean}")
        print("grade distribution")
        for i in range(5, 0, -1):  # Stops at 1, skips 0
            print(f"{i}: " + "x" * self.__grades[i])


class CourseRecordsApplication:
    def __init__(self):
        self.__course_records = CourseRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__course_records.add_course(course, grade, credits)

    def get_course_data(self):
        course = input("course: ")
        if self.__course_records.get_course_data(course) is None:
            print("no entry for this course")
            return
        grade, credits = self.__course_records.get_course_data(course)
        print(f"{course} ({credits} cr) grade {grade}")

    def statistics(self):
        self.__course_records.stats()

    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()


app = CourseRecordsApplication()
app.execute()
