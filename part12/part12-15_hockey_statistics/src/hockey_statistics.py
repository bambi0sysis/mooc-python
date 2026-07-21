import json

filename = input("file name: ")
with open(filename) as file:
    content = file.read()
data = json.loads(content)


def help():
    string = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
    print(string)


def search_for_player():
    name = input("name: ")
    for player in data:
        if player["name"] == name:
            print(
                f"{player['name']:21}{player['team']:5}{player['goals']:>2} + {player['assists']:>2} = {player['goals'] + player['assists']:>3}"
            )


def teams():
    teams_set = []
    for player in data:
        if player["team"] not in teams_set:
            teams_set.append(player["team"])
    teams_set.sort()
    for team in teams_set:
        print(team)


def countries():
    countries_set = []
    for player in data:
        if player["nationality"] not in countries_set:
            countries_set.append(player["nationality"])
    countries_set.sort()
    for team in countries_set:
        print(team)


def players_in_team():
    team = input("team: ")
    team_players = []
    for player in data:
        if player["team"] == team:
            team_players.append(player)
    team_players.sort(key=lambda d: d["goals"] + d["assists"], reverse=True)
    for player in team_players:
        print(
            f"{player['name']:21}{player['team']:5}{player['goals']:>2} + {player['assists']:>2} = {player['goals'] + player['assists']:>3}"
        )


def players_from_country():
    country = input("country: ")
    team_players = []
    for player in data:
        if player["nationality"] == country:
            team_players.append(player)

    team_players.sort(key=lambda d: d["goals"] + d["assists"], reverse=True)
    for player in team_players:
        print(
            f"{player['name']:21}{player['team']:5}{player['goals']:>2} + {player['assists']:>2} = {player['goals'] + player['assists']:>3}"
        )


def most_points():
    how_many = int(input("how many: "))
    most_points_data = data
    data.sort(key=lambda d: (d["assists"] + d["goals"], d["goals"]), reverse=True)
    i = j = 0
    while i < how_many:
        while j < len(most_points_data):
            print(
                f"{most_points_data[j]['name']:21}{most_points_data[j]['team']:5}{most_points_data[j]['goals']:>2} + {most_points_data[j]['assists']:>2} = {most_points_data[j]['goals'] + most_points_data[j]['assists']:>3}"
            )
            j += 1
            i += 1
            break


def most_goals():
    how_many = int(input("how many: "))
    most_goals_data = data
    data.sort(key=lambda d: (-d["goals"], d["games"]))
    i = j = 0
    while i < how_many:
        while j < len(most_goals_data):
            print(
                f"{most_goals_data[j]['name']:21}{most_goals_data[j]['team']:5}{most_goals_data[j]['goals']:>2} + {most_goals_data[j]['assists']:>2} = {most_goals_data[j]['goals'] + most_goals_data[j]['assists']:>3}"
            )
            j += 1
            i += 1
            break


print(f"read the data of {len(data)} players")
help()
while True:
    print()
    command = input("command: ")
    if command == "0":
        break
    elif command == "1":
        search_for_player()
    elif command == "2":
        teams()
    elif command == "3":
        countries()
    elif command == "4":
        players_in_team()
    elif command == "5":
        players_from_country()
    elif command == "6":
        most_points()
    elif command == "7":
        most_goals()
    else:
        help()
