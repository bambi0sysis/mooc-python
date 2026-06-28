import csv
from datetime import datetime, timedelta


def processing_files():
    cheaters = []

    start_times = {}
    with open("start_times.csv") as file:
        for info_person in csv.reader(file, delimiter=";"):
            start_times[info_person[0]] = datetime.strptime(
                f"{'2000:12:1'}:{info_person[1]}", "%Y:%m:%d:%H:%M"
            )
    students = []
    for val in start_times.keys():
        students.append(val)

    submissions = {}
    for student in students:
        submissions[student] = {}

    with open("submissions.csv") as file:
        for info_person in csv.reader(file, delimiter=";"):
            person = info_person[0]
            task = int(info_person[1])
            points = int(info_person[2])
            time = datetime.strptime(
                f"{'2000:12:1'}:{info_person[3]}", "%Y:%m:%d:%H:%M"
            )

            if time - start_times[person] > timedelta(hours=3):
                if person not in cheaters:
                    cheaters.append(person)
            else:
                if person in cheaters:
                    cheaters.remove(person)

            if person not in cheaters:
                if task in submissions[person] and points > submissions[person][task]:
                    submissions[person][task] = points
                elif task not in submissions[person] and person not in cheaters:
                    submissions[person][task] = points

    return submissions


def final_points():
    final_points = {}

    data = processing_files()
    for person, dic in data.items():
        points = 0
        for task in dic:
            points += int(dic[task])
        final_points[person] = points

    return final_points
