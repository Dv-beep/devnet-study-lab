import requests

BASE_URL = "http://localhost:3000"

employee_id = 1
door_id = 1

employee_response = requests.get(f"{BASE_URL}/employees/{employee_id}")
employee = employee_response.json()

if employee["badgeStatus"] == "suspended":
    status = "denied"
    
else:
    status = "granted"
    
access_log = {
    "employeeId": employee_id,
    "doorId": door_id,
    "status": status
}

response = requests.post(f"{BASE_URL}/access-logs", json=access_log)

print(f"badge status: {employee['badgeStatus']})")
print(f"access status: {status}")
print(response.json())
