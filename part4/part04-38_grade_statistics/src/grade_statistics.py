def grade(points):
    limit = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= limit[i]:
            return i

def main():
    points = []
    grades = [0] * 6
    while True:
        
        # input
        student_data = input("Exam points and exercises completed: ").split()
        if not student_data:
            break
        student_data[0] = int(student_data[0])
        student_data[1] = int(student_data[1]) // 10

        total_points = student_data[0] + student_data[1]
        points.append(total_points)
        
        grd = grade(total_points)
        if student_data[0] < 10:
            grd = 0
        grades[grd] += 1

        # testing
        # print(student_data, total_points, grd, grades)

    print("Statistics:")
    print(f"Points average: {sum(points) / len(points):.1f}")
    print(f"Pass percentage: {100 * (len(points) - grades[0]) / len(points):.1f}")
    print("Grade distribution: ")
    for i in range(5, -1, -1):
        star = "*" * grades[i]
        print(f"  {i}: {star}")

main()

# def inputs():
#     points = []
#     point = input("Exam points and exercises completed: ").split(" ")
#     points.append(point)
#     while point:
#         point = input("Exam points and exercises completed: ")
#         point_split = point.split(" ")
#         points.append(point_split)
#     points.pop()
#     # print(points)
#     return points

# def exercise_points(points):
#     for i in range(len(points)):
#         # exercise_points = 10
#         # print(points[i][1])
#         exercise = int(points[i][1]) // 10
#         # if exercise >= 9 * 10:
#         #     exercise_points = 9
#         # elif exercise >= 8 * 10:
#         #     exercise_points = 8
#         # elif exercise >= 7 * 10:
#         #     exercise_points = 7
#         # elif exercise >= 6 * 10:
#         #     exercise_points = 6
#         # elif exercise >= 5 * 10:
#         #     exercise_points = 5
#         # elif exercise >= 4 * 10:
#         #     exercise_points = 4
#         # elif exercise >= 3 * 10:
#         #     exercise_points = 3
#         # elif exercise >= 2 * 10:
#         #     exercise_points = 2
#         # elif exercise >= 1 * 10:
#         #     exercise_points = 1
#         # else:
#         #     exercise_points = 0
#         # if int(points[i][0]) < 10:
#         #     points[i][0] = 0
#         points[i][1] = exercise
#         # print(exercise_points)
#         # print(points[i])
#     # print(points)
#     return points

# def pass_percentage(points: list):
#     grades = []
#     for i in range(len(points)):
#         f_points = int(points[i][0]) + int(points[i][1])
#         if 0 <= f_points <= 14 or int(points[i][0]) < 10:
#             grade = 0
#         elif f_points <= 17:
#             grade = 1
#         elif f_points <= 20:
#             grade = 2
#         elif f_points <= 23:
#             grade = 3
#         elif f_points <= 27:
#             grade = 4
#         else:
#             grade = 5
#         grades.append(grade)
#     # print(grades)
#     return grades

# def outputs(points: list, grades: int):
#     for i in range(len(points)):
#         points[i] = int(points[i][0]) + int(points[i][1])
#     print("Statistics:")
#     # for i in range(len(points)):
#     avg = f"{sum(points) / len(points):.1f}"
#     print("Points average:", avg)
#     percentage = f"{((len(grades) - grades.count(0)) / len(grades)) * 100:.1f}"
#     print("Pass percentage:", percentage)
#     print("Grade distribution:")
#     for x in range(5, -1, -1):
#         if grades.count(x) == -1:
#             star = 0
#         else:
#             star = grades.count(x)
#         # if i == 1:
#         #    print(f"{i:3}:{"*" * star:^3}")
#         # elif i == 2:
#         print(f"{x:3}: {"*" * star}")

# inputing = inputs()
# final_points = exercise_points(inputing)
# grading = pass_percentage(final_points)
# outputs(final_points, grading)