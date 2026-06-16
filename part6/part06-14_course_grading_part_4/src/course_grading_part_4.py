info_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")
course = input("Course information: ")

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

grade_pts = {id: (exercises[id]*10)//40 + exam_pts[id] for id in exercises if id in exam_pts}

def grade(points):
    a = 0 
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
    return a

with open(course) as file1, open('results.txt', 'w') as file:
    c = []
    for line in file1:
        line = line.split(':')[1].strip()
        c. append(line)

    file.write(f'{c[0]}, {c[1]} credits\n')
    file.write('='*38 + '\n')
    file.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
    for id, name in names.items():
        if id in exercises:
            file.write(f"\n{name:30}{exercises[id]:<10}{exercises[id] // 4 :<10}{exam_pts[id]:<10}{grade_pts[id]:<10}{grade(grade_pts[id]):<10}")

with open("results.csv", 'w') as file:
    for id, pts in grade_pts.items():
        file.write(f'{id};{names[id]};{grade(grade_pts[id])}\n')