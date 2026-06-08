# if False:
#     info_file = input("Student information: ")
#     exercise_file = input("Exercises completed: ")
# else:
#     info_file = "students1.csv"
#     exercise_file = 'exercises1.csv'

info_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

names = {}

with open(info_file) as file:
    for line in file:
        line = line.strip().split(";")
        if line[0] == 'id':
            continue
        names[line[0]] = line[1] + " " + line[2]

exercises = {}

with open(exercise_file) as file:
    for line in file: 
        count = 0
        line = line.strip().split(';')
        if line[0] == 'id':
            continue
        for exercise in line[1:]:
            count += int(exercise)
        exercises[line[0]] = count

for id, name in names.items():
    if id in exercises:
        print(name, exercises[id])