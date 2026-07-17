class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (
            f"BallPlayer(name={self.name}, number={self.number}, "
            f"goals={self.goals}, passes={self.passes}, minutes={self.minutes})"
        )


def most_goals(players: list):
    most_goals_by = [(player.name, player.goals) for player in players]
    most_goals_by.sort(key=lambda t: t[1])
    return most_goals_by[-1][0]


def most_points(players: list):
    players_data = [
        (player.name, player.number, player.goals + player.passes) for player in players
    ]
    players_data.sort(key=lambda t: t[-1])
    return players_data[-1][0], players_data[-1][1]


def least_minutes(players: list):
    least_min = [(player, player.minutes) for player in players]
    least_min.sort(key=lambda t: t[-1])
    return least_min[0][0]
