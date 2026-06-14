import json
import requests

BASE_URL = "http://localhost:3000"

headers = {
    "Authorization": "Bearer your_token_here"
}

response = requests.get(f"{BASE_URL}/devices", headers=headers)

print(f"Status Code: {response.status_code}")
print("Response:")
print(json.dumps(response.json(), indent=4))