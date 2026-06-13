import json
import requests

BASE_URL = "http://localhost:3000"

for i in range(1,11):
    
    devices = {
        "hostname"  :   f"sw-access-{i:02}",
        "ipAddress" :   f"10.1.1.{i}",
        "status"    :   "online"
    }

    requests.post(f"{BASE_URL}/devices", json=devices)

print(f"Status Code: {requests.status_codes}")
print("Devices added to endpoint /devices")