from helpers import *

if not environ.get('SPOONACULAR_API_KEY') or not environ.get('GEMINI_API_KEY'):
    print("Can't access at least one necessary API key, exiting.")
    exit(1)


recipe_list = get_recipes()
recipe_info_list = get_recipe_info(recipe_list)

print(type(recipe_list), type(recipe_info_list))