import json
import requests

BASE_URL = "http://localhost:3000"

devices = requests.get(f"{BASE_URL}/devices").json()

for device in devices:
    if device['ipAddress'] == "10.1.1.3":
        device['status'] = 'offline'
        
        response = requests.patch(f"{BASE_URL}/devices/{device['id']}", json=device)
        print(f"Status Code: {response.status_code}")