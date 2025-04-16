import requests
from skimage import io
import matplotlib.pyplot as plt
from utils import load_api_key

def get_apod_image():
    api_key = load_api_key()
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key}

    response = requests.get(url, params=params)
    data = response.json()

    # Headers de limite
    print("Limite total:", response.headers.get('X-RateLimit-Limit'))
    print("Restantes:", response.headers.get('X-RateLimit-Remaining'))

    print("\n📸 Title:", data["title"])
    print("📝 Explanation:", data["explanation"])
    print("© Copyright:", data.get("copyright", "N/A"))

    img_url = data.get("hdurl") or data["url"]
    img = io.imread(img_url)

    plt.imshow(img)
    plt.axis("off")
    plt.title(data["title"])
    plt.show()

if __name__ == "__main__":
    get_apod_image()
