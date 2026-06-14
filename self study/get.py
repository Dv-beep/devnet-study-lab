import requests
import json

BASE_URL = "http://localhost:3000"

response = requests.get(f"{BASE_URL}/devices")

print(f"Status Code {requests.status_codes}")
print("Response:")
print(response.json())