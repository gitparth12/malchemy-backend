import requests
import json
from os import environ

RECIPE_SEARCH_URL = "https://api.spoonacular.com/recipes/complexSearch"
RECIPE_INFO_URL = "https://api.spoonacular.com/recipes/informationBulk"

SPOONACULAR_API_KEY = environ.get('SPOONACULAR_API_KEY')
GEMINI_API_KEY = environ.get('GEMINI_API_KEY')

if not environ.get('SPOONACULAR_API_KEY') or not environ.get('GEMINI_API_KEY'):
    print("Can't access at least one necessary API key, exiting.")
    exit(1)

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
    print(json.dumps(response.json(), indent=2))
else:
    print("Error:", response.status_code, response.text)
