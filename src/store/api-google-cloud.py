import requests
import base64
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
IMAGE_PATH = "example-3.jpg"

with open(IMAGE_PATH, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

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

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    try:
        labels = response.json().get("responses", [])[0].get("labelAnnotations", [])
        
        if labels:
            filtered_labels = [label for label in labels if label['score'] >= 0.7]
            
            if filtered_labels:
                filtered_labels.sort(key=lambda x: x['score'], reverse=True)
                
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