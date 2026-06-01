import requests

BASE_URL = "http://localhost:3000"

# GET all alerts
response = requests.get(f"{BASE_URL}/devices")

devices = response.json()

# Loop through devices and print alerts
for device in devices:
    # Check for offline devices
    if device["status"] == "offline":
        print(f'{device["hostname"]} is OFFLINE')
        
        # Create alert object        
        alert = {
            "severity": "high",
            "source": device["hostname"],
            "message": f"Device {device['hostname']} is offline"
        }

        # POST alert to API
        alert_response = requests.post(
            f"{BASE_URL}/alerts",
            json=alert
        )
        
        print("Alert created:")
        print(alert_response.json())
