import requests
import json
from os import environ

RECIPE_SEARCH_URL = "https://api.spoonacular.com/recipes/complexSearch"
RECIPE_INFO_URL = "https://api.spoonacular.com/recipes/informationBulk"

SPOONACULAR_API_KEY = environ.get('SPOONACULAR_API_KEY')
GEMINI_API_KEY = environ.get('GEMINI_API_KEY')

def get_recipes():
    params = {
        "includeIngredients": "chicken,tomato,basil,garlic,onion,carrot,broccoli,\
                mushroom,cheese,eggs,rice,pasta,beans,spinach,cilantro,lemon,avocado",
        "cuisine": "italian,mexican",
        "intolerances": "shellfish,peanuts",
        "number": 10,
        "sort": "meta-score",
        "apiKey": SPOONACULAR_API_KEY,
    }

    response = requests.get(RECIPE_SEARCH_URL, params=params)

    if response.status_code == 200:
        response = response.json()
        print(f'Fetched {len(response)} recipes, moving onto full information\n')
        return response

    print("Error:", response.status_code, response.text)
    exit(1)


def get_recipe_info(recipe_list):
    recipe_ids = [x['id'] for x in recipe_list]

    params = {
        "ids": ','.join(map(str, recipe_ids)),
        "includeNutrition": True,
        "apiKey": SPOONACULAR_API_KEY,
    }

    response = requests.get(RECIPE_INFO_URL, params=params)
    if response.status_code == 200:
        response = response.json()
        print(f'Fetched full recipe information for {len(response)} recipes.')

        # Write recipe info in a file for testing
        response = json.dumps(response.json(), indent=2)
        with open('recipes_info.json', 'w') as f:
            f.write(response)

        return response
    else:
        print('Error:', response.status_code, response.text)
        exit(1)

    
