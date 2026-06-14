import math
def get_station_data(filename: str):
    stations_names = {}
    with open(filename) as file:
        for line in file:
            line = line.strip().split(';')
            if line[0] == 'Longitude':
                continue
            stations_names[line[3]] = (float(line[0]), float(line[1]))
    return stations_names

# st = {}
# line = "24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;1".strip().split(';')
# print(line)
# st[line[3]] = (float(line[0]), float(line[1]))
# print(st)
# print(list(st))

def distance(stations: dict, station1: str, station2: str):
    longitude1, longitude2 = stations[station1][0], stations[station2][0]
    latitude1, latitude2 = stations[station2][1], stations[station1][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    stations_name = list(stations)
    stations_without_1st = {name: stations[name] for name in stations_name[1:]}

    greatest_dis = 0.0
    st1 = ""
    st2 = ""
    for i in stations:
        for j in stations_without_1st:
            if distance(stations, i, j) > greatest_dis:
                greatest_dis = distance(stations, i, j)
                st1 = i
                st2 = j
    
    return st1, st2, greatest_dis
