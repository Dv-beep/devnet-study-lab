import requests

BASE_URL = "http://localhost:3000"

for i in range(1, 101):
    devices = {
        "hostname": f"sw-access-{i:03}",
        "ipAddress": f"10.1.1.{i}",
        "status": "online",
        "vendor": "Cisco",
        "model": "Catalyst 9300",
        
    }
    response = requests.post(f"{BASE_URL}/devices", json=devices)
    print(response.status_code, devices["hostname"], response.json())