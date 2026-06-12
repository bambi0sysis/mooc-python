def store(filename: str):
    recipes = []

    with open(filename) as file:
        single_recipe = []
        for line in file:
            if line == '\n':
                recipes.append(single_recipe)
                single_recipe = []
                continue
            single_recipe.append(line.strip())
            
        if single_recipe:
            recipes.append(single_recipe)

    return recipes

def search_by_name(filename: str, word: str):
    recipes = store(filename)

    similar_search = []    
    for recipe in recipes:
        if word in recipe[0].strip().replace(" ", "").lower():
            similar_search.append(recipe[0])

    return similar_search 

def search_by_time(filename: str, prep_time: int):
    recipes = store(filename)
    
    similar_search = []    
    for recipe in recipes:
        if int(recipe[1]) <= prep_time:
            similar_search.append(f'{recipe[0]}, preparation time {recipe[1]} min')
    # print(similar_search)

    return similar_search

def search_by_ingredient(filename: str, ingredient: str):
    recipes = store(filename)

    similar_search = []    
    for recipe in recipes:
        recipe_formatted = [Str.lower() for Str in recipe[2:]]
        if ingredient in recipe_formatted:
            similar_search.append(f'{recipe[0]}, preparation time {recipe[1]} min')

    return similar_search 