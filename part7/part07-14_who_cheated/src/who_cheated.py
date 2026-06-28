from datetime import datetime, timedelta


def cheaters():
    cheaterss = []

    start_times = {}
    with open("start_times.csv") as file:
        for line in file:
            line = line.strip().split(";")
            start_times[line[0]] = datetime.strptime(
                f"{'2000:12:1'}:{line[1]}", "%Y:%m:%d:%H:%M"
            )

    exam_time = timedelta(hours=3)

    with open("submissions.csv") as file:
        for row in file:
            row = row.strip().split(";")
            if row[0] in start_times:
                time_taken = (
                    datetime.strptime(f"{'2000:12:1'}:{row[3]}", "%Y:%m:%d:%H:%M")
                    - start_times[row[0]]
                )
                if time_taken > exam_time:
                    if row[0] not in cheaterss:
                        cheaterss.append(row[0])

    return cheaterss
