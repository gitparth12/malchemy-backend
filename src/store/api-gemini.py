from google import genai
from google.genai import types
import PIL.Image

image = PIL.Image.open('example-1.jpg')

client = genai.Client(api_key="AIzaSyAH19SRtepMWTD9YQmm0YMbfs-aHrOxe9o")

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=[{"text": "What foods/ingredients are in this image? The answer should be either one word or a comma-separated and capitalised list of words."}, image]  # Asking a question about the image
)

print(response.text)