from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from helpers import *

UPLOAD_FOLDER = 'data/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/hello', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api/recipes", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image = request.files["image"]

    if image.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    
    # Save the image
    image_path = path.join(IMAGE_DIR, image.filename)
    image.save(image_path)

    ingredients = get_ingredients_from_image(image_path)
    recipe_list = get_recipes(ingredients=ingredients)
    recipe_info_list = get_recipe_info(recipe_list)
    json_list = get_filtered_recipe_json(recipe_info_list)
    return jsonify(json_list)


if __name__ == '__main__':
    if not (SPOONACULAR_API_KEY and GEMINI_API_KEY):
        print("Can't access at least one necessary API key, exiting.")
        exit(1)

    app.run(debug=True)