def add_student(students: dict, name: str):
    students[name] = {}
    
def print_student(students: dict, name: str):
    if name in students:
        if len(students[name]) == 0:
            print(f"{name}:")
            print(" no completed courses")
            return
        print(f"{name}:")
        print(f" {len(students[name])} completed courses:")
        grade = 0
        for k,v in students[name].items():
            print(f"  {k} {v}")
            grade += v
        print(f" average grade {grade / len(students[name]):.1f}")
        return
    print(f"{name}: no such person in the database")
    return

def add_course(students: dict, name: str, course: tuple):
    if course[1] == 0:
        return
    if course[0] in students[name]:
        if course[1] <= students[name][course[0]]:
            return
        else:
            students[name][course[0]] = course[1]
            return
    students[name][course[0]] = course[1]

def summary(students: dict):
    print("students", len(students))
    most_courses = 0
    most_by = ""
    for name in students:
        if len(students[name]) > most_courses:
            most_courses = len(students[name])
            most_by = name
    print(f"most courses completed {most_courses} {most_by}")
    best_grade = 0
    best_by = ""
    for name in students:
        grade = 0
        for _, v in students[name].items():
            grade += v
        if len(students[name]) == 0:
            continue
        if best_grade < grade / len(students[name]):
            best_grade = grade / len(students[name])
            best_by = name
        
    print(f"best average grade {best_grade} {best_by}")

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")    
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# def add_student(students: dict, name: str):
#     students[name] = []

# def print_student(students: dict, name: str):
#     if name in students:
#         print(f"{name}:")
#         if not students[name]:
#             print(" no completed courses")
#         else:
#             print(f" {len(students[name])} completed courses:")
#             grade = 0
#             for i in range(len(students[name])):
#                 grade += students[name][i][1]
#                 print(f"  {students[name][i][0]} {students[name][i][1]}")
#             print(f" average grade {grade/len(students[name]):.1f}")
#     else:
#         print(f"{name}: no such person in the database")

# def add_course(students: dict, name: str, course: tuple):
#     if course[1] == 0:
#         return
#     courses = students[name]
#     for i in range(len(courses)):
#         if courses[i][0] == course[0]:
#             if course[1] > courses[i][1]:
#                 courses[i] = course
#             return
#     courses.append(course)

# def summary(students: dict):
#     print(f'students {len(students)}')

#     max_courses = 0
#     winner = ""
#     for name in students:
#         count = len(students[name])
#         if count > max_courses:
#             max_courses = count
#             winner = name
#     print(f"most courses completed {max_courses} {winner}")

#     best_avg = 0
#     topper = ""
#     for name in students:
#         grade = 0
#         for i in range(len(students[name])):
#             grade += students[name][i][1]
#             grd = grade / len(students[name])
#             if grd > best_avg:
#                 best_avg = grd
#                 topper = name
#     print(f"best average grade {best_avg} {topper}")
