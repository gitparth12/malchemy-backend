from helpers import *

if not (SPOONACULAR_API_KEY and GEMINI_API_KEY):
    print("Can't access at least one necessary API key, exiting.")
    exit(1)


ingredients = get_ingredients_from_image('test-images/example-3.jpg')

if not path.exists('recipes_info.json'):
    recipe_list = get_recipes(ingredients=ingredients)
    recipe_info_list = get_recipe_info(recipe_list)
else:
    print('Recipe info already saved, skipping API calls. Disable this code in production.')
    recipe_info_list = json.load(open('recipes_info.json'))
    print(ingredients)

save_recipes_md(recipe_info_list)
