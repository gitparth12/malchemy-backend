import requests
from os import environ

RECIPE_SEARCH_URL = "https://api.spoonacular.com/recipes/complexSearch"
RECIPE_INFO_URL = "https://api.spoonacular.com/recipes/informationBulk"

if not environ.get('SPOONACULAR_API_KEY') or not environ.get('GEMINI_API_KEY'):
    print("Can't access at least one necessary API key, exiting.")
    exit(1)



