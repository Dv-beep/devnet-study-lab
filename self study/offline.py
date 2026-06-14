import json
import requests

BASE_URL = "http://localhost:3000"

devices = requests.get(f"{BASE_URL}/devices").json()

for device in devices:
    if device['status'] == "offline":
        response = requests.get(f"{BASE_URL}/devices/{device['id']}")
        print(f"Status Code: {response.status_code}")
        print("Response:")
        print(json.dumps(response.json(), indent=4))