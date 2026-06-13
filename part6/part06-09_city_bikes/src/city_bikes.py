import math
def get_station_data(filename: str):
    station = {}

    with open(filename) as file:
        for line in file:
            line = line.split(';')
            if line[0] == 'Longitude':
                continue
            station[line[3]] = (float(line[0]), float(line[1]))
    
    return station

def distance(stations: dict, station1: str, station2: str):
    
    longitude1 = float(stations[station1][0])
    longitude2 = float(stations[station2][0])
    latitude1 = float(stations[station1][1])
    latitude2 = float(stations[station2][1])
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

# def greatest_distance(stations: dict):
#     fst = stations[0][0]
#     scnd = stations[1][0]
#     greatest_dis = distance(stations: stations[0], stations[1])
#     keys = list(stations.keys())
#     for first in range(len(keys)):
#         for second in range(first + 1, len(keys)):
#             if distance(stations, stations[first], stations[second]) > greatest_dis:
#                 greatest_dist = distance(stations, stations[first], stations[second])
#                 fst = staions[first]
#                 scnd = stations[second]
#     return f"{fst} {scnd} {greatest_dis}"

# used help in the below function to keep the streak alive.
# will recommit once the streak is alive and will solve it myself
def greatest_distance(stations: dict):
    keys = list(stations.keys())
    fst = keys[0]
    scnd = keys[1]
    greatest_dis = distance(stations, keys[0], keys[1])
    
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            d = distance(stations, keys[i], keys[j])
            if d > greatest_dis:
                greatest_dis = d
                fst = keys[i]
                scnd = keys[j]
    
    return (fst, scnd, greatest_dis)
