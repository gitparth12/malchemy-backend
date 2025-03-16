from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from helpers import *

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image = request.files["image"]

    if image.filename == "":
        return jsonify({"error": "Empty filename"}), 400
    
    # Save the image
    image_path = path.join(app.config["UPLOAD_FOLDER"], image.filename)
    image.save(image_path)

    # Example: Open the image with Pillow and get size
    with Image.open(image_path) as img:
        width, height = img.size

    return jsonify({"message": "Image uploaded successfully", "width": width, "height": height})

if __name__ == '__main__':
    app.run(debug=True)