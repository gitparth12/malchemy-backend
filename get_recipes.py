from helpers import *

if not (SPOONACULAR_API_KEY and GEMINI_API_KEY):
    print("Can't access at least one necessary API key, exiting.")
    exit(1)


if not path.exists('recipes_info.json'):
    recipe_list = get_recipes()
    recipe_info_list = get_recipe_info(recipe_list)
else:
    print('Recipe info already saved, skipping API calls. Disable this code in production.')
    recipe_info_list = json.load(open('recipes_info.json'))
    save_recipes_md(recipe_info_list)
