import requests
from skimage import io
import matplotlib.pyplot as plt
from utils import load_api_key

def get_rover_photos(rover="curiosity", sol=1000, cameras=None):
    api_key = load_api_key()
    page = 1
    cameras = cameras or ["FHAZ", "RHAZ", "NAVCAM"]

    while True:
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
        params = {
            'sol': sol,
            'page': page,
            'api_key': api_key
        }

        response = requests.get(url, params=params)
        photos = response.json()["photos"]

        if not photos:
            print("✅ Fim das fotos.")
            break

        for photo in photos:
            if photo["camera"]["name"] in cameras:
                print(f"📄 Página {page} | 📷 {photo['camera']['name']} | ID {photo['id']}")
                img = io.imread(photo["img_src"])
                plt.imshow(img)
                plt.axis("off")
                plt.title(f"Page {page} | Camera: {photo['camera']['name']} | ID: {photo['id']}")
                plt.show()

        page += 1

if __name__ == "__main__":
    sol = int(input("Informe o número do sol (ex: 1000): "))
    get_rover_photos(sol=sol)
