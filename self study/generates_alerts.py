import random
import time
import requests

BASE_URL = "http://localhost:3000"

severities = ["low", "medium", "high", "critical"]
sources = ["Firewall", "XDR", "VPN", "SIEM"]
message = [
    "Suspicious login attempt detected",
    "Malware detected on endpoint",
    "Unusual network traffic observed",
    "Multiple failed login attempts",
    "Data exfiltration attempt detected",
    "Unauthorized access to sensitive data",
]
hostname = ("switch-01", "router-01", "firewall-01", "server-01")

while True:
    alert = {
        "severity": random.choice(severities),
        "source": random.choice(sources),
        "message": random.choice(message),
        "hostname": random.choice(hostname)
    }
    
    response = requests.post(f"{BASE_URL}/alerts", json=alert)
    
    print(response.status_code, response.json())
    
    time.sleep(5.0)  # Wait for 5 seconds before sending the next alert