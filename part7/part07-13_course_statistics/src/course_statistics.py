import urllib.request
import json
from math import floor


def retrieve_all():
    response = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    )
    content = response.read()
    courses = json.loads(content)
    result = []

    for course in courses:
        if course["enabled"]:
            result.append(
                (
                    course["fullName"],
                    course["name"],
                    course["year"],
                    sum(course["exercises"]),
                )
            )

    return result


def retrieve_course(course_name: str):
    response = urllib.request.urlopen(
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )
    courses = json.loads(response.read())
    result = {"weeks": len(courses)}

    max_student = total_student = total_hours = exercises_total = 0
    for course in courses.values():
        if course["students"] > max_student:
            max_student = course["students"]
            total_student += course["students"]

        total_hours += course["hour_total"]
        exercises_total += course["exercise_total"]

    result["students"] = max_student
    result["hours"] = total_hours
    result["hours_average"] = floor(total_hours / total_student)
    result["exercises"] = exercises_total
    result["exercises_average"] = floor(exercises_total / total_student)

    return result
