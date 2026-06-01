import requests

devices = requests.get("http://localhost:3000/devices").json()

offline_devices = [
    device for device in devices
    if device["status"] == "offline"
]

print(offline_devices)