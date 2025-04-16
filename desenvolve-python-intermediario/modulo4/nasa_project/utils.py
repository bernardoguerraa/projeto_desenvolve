import json

def load_api_key(path="key.json"):
    with open(path) as f:
        return json.load(f)["API_KEY"]
