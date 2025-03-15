import requests
from os import environ

if not environ.get('SPOONACULAR_API_KEY') or not environ.get('GEMINI_API_KEY'):
    print("Can't access at least one necessary API key, exiting.")
    exit(1)



