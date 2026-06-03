def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {"name": name, 
        "director": director, 
        "year": year, 
        "runtime": runtime}
    database.append(movie)

# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)