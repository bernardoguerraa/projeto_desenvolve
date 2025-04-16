import requests
from utils import load_api_key

def get_rover_manifest(rover="curiosity"):
    api_key = load_api_key()
    url = f"https://api.nasa.gov/mars-photos/api/v1/manifests/{rover}"
    params = {'api_key': api_key}

    response = requests.get(url, params=params)
    data = response.json()["photo_manifest"]

    print("🛠 Rover:", data["name"])
    print("🔴 Último sol:", data["max_sol"])
    print("📅 Última data terrestre:", data["max_date"])

    return data["max_sol"]

if __name__ == "__main__":
    get_rover_manifest()
