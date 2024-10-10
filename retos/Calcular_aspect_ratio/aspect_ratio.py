import requests
import math
from PIL import Image
from io import BytesIO

def calcular_aspect_ratio_url(url):

    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    width, height = image.size
    gcd = math.gcd(width, height) # Máximo común divisor

    width = int(width/gcd)
    height = int(height/gcd)

    print(f"Aspect ratio: {width}:{height}")


url = "https://cdn.pixabay.com/photo/2022/08/28/01/40/cyberpunk-city-7415576_1280.jpg"
calcular_aspect_ratio_url(url)


