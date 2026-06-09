info_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

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

exam_pts = {}

with open(exam_file) as file:
    for line in file:
        line = line.strip().split(';')
        if line[0] == 'id':
            continue
        score = 0
        for pts in line[1:]:
            score += int(pts)
        exam_pts[line[0]] = score

# grade_pts = {}
# for id in exercises:
#     if id in exam_pts:
#         grade_pts[id] = (exercises[id]*10)//40 + exam_pts[id]
# grade_pts = [for id in exercises if id in exam_pts (exercises[id]*10)//40 + exam_pts[id]]
# asked chatgpt for syntax of dict comprehension

# was a bit confused in getting the below formula
grade_pts = {id: (exercises[id]*10)//40 + exam_pts[id] for id in exercises if id in exam_pts}

# again to avoid if statements and do it cleanly i thought of this idea. but asked gpt for help. 
# idea: { (0,15): 0, (15,.. etc??. but i wasnt satisfied with gpt. so switched to if/else
# grade = {id: }

grade = {}
for id, grd in grade_pts.items():
    if grd >= 28:
        grade[id] = 5
    elif grd >= 24:
        grade[id] = 4
    elif grd >= 21:
        grade[id] = 3
    elif grd >= 18:
        grade[id] = 2
    elif grd >= 15:
        grade[id] = 1
    else:
        grade[id] = 0

for id, name in names.items():
    if id in exercises:
        print(name, grade[id])

