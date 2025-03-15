import requests
import base64
import os

# Load the API key from environment variables (for security)
API_KEY = os.getenv("GOOGLE_API_KEY")  # Set this in your environment variables
IMAGE_PATH = "example-3.jpg"

# Convert image to base64
with open(IMAGE_PATH, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

# API request
url = f"https://vision.googleapis.com/v1/images:annotate?key={API_KEY}"
headers = {"Content-Type": "application/json"}
data = {
    "requests": [
        {
            "image": {"content": image_base64},
            "features": [{"type": "LABEL_DETECTION"}]
        }
    ]
}

# Make the API request
response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Extract the detected labels and their confidence scores
        labels = response.json().get("responses", [])[0].get("labelAnnotations", [])
        
        if labels:
            # Filter labels that are food-related based on confidence
            # You can adjust the confidence threshold if needed (e.g., 0.7)
            filtered_labels = [label for label in labels if label['score'] >= 0.7]
            
            if filtered_labels:
                # Sort labels based on confidence score (highest first)
                filtered_labels.sort(key=lambda x: x['score'], reverse=True)
                
                # Print all food-related labels
                print("Detected Ingredients:")
                for label in filtered_labels:
                    print(f"- {label['description']} (Confidence: {label['score']:.2f})")
            else:
                print("No food-related labels detected with sufficient confidence.")
        else:
            print("No labels detected.")
    except ValueError:
        print("Error parsing response.")
else:
    print(f"Error: {response.status_code}, {response.text}")