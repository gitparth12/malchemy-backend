import requests
import json
from dotenv import load_dotenv
from os import environ, path, makedirs
from google import genai
import PIL.Image

load_dotenv()

RECIPE_SEARCH_URL = "https://api.spoonacular.com/recipes/complexSearch"
RECIPE_INFO_URL = "https://api.spoonacular.com/recipes/informationBulk"

SPOONACULAR_API_KEY = environ.get('SPOONACULAR_API_KEY')
GEMINI_API_KEY = environ.get('GEMINI_API_KEY')

def get_recipes(ingredients="chicken,tomato,basil,garlic") -> list:
    params = {
        "includeIngredients": ingredients,
        "cuisine": "italian,mexican",
        "intolerances": "shellfish,peanuts",
        "number": 10,
        "sort": "meta-score",
        "apiKey": SPOONACULAR_API_KEY,
    }

    response = requests.get(RECIPE_SEARCH_URL, params=params)

    if response.status_code == 200:
        response = response.json()['results']
        print(f'Fetched {len(response)} recipes, moving onto full information\n')
        return response

    print("Error:", response.status_code, response.text)
    exit(1)


def get_recipe_info(recipe_list) -> list:
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
        response_string = json.dumps(response, indent=2)
        with open('recipes_info.json', 'w') as f:
            f.write(response_string)

        return response
    else:
        print('Error:', response.status_code, response.text)
        exit(1)

    
def save_recipes_md(recipe_info_list):
    if not path.exists('data/recipes'):
        makedirs('data/recipes')
    
    for i, recipe in enumerate(recipe_info_list):
        with open(f'data/recipes/{i}_info.md', 'w') as md_file:
            md_file.write("# Recipe Information\n\n")
            
            # Iterate over the recipes and write information to the Markdown file
            # Recipe title and image
            md_file.write(f"## {recipe['title']}\n")
            md_file.write(f"![{recipe['title']}]({recipe['image']})\n\n")
            md_file.write(f"**Cooking Time:** {recipe['readyInMinutes']} minutes\n")
            md_file.write(f"**Servings:** {recipe['servings']}\n")
            
            # Nutrition Information
            md_file.write("### Nutrition Information:\n")
            for nutrient in recipe['nutrition']['nutrients']:
                md_file.write(f" - **{nutrient['name']}:** {nutrient['amount']} {nutrient['unit']}\n")
            md_file.write("\n")
            
            # Instructions
            md_file.write("### Instructions:\n")
            md_file.write(f"{recipe['instructions']}\n\n")
            
            # Ingredients
            md_file.write("### Ingredients:\n")
            for ingredient in recipe['extendedIngredients']:
                md_file.write(f" - {ingredient['amount']} {ingredient['unit']} {ingredient['name']}\n")
            
            # Separator between recipes
            md_file.write("\n---\n\n")


def get_ingredients_from_image(image_path):
    if not path.exists(image_path):
        print("Image doesn't exist. Please check provided path.")
        exit(1)

    image = PIL.Image.open(image_path)
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=[{"text": "What foods/ingredients are in this image? The answer should be either one word or a comma-separated and capitalised list of words."}, image]  # Asking a question about the image
    )

    return response.text


