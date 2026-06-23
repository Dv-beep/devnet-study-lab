import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "devnetsandboxiosxec8k.cisco.com"
USER = "christiantech03"
PASS = "BPt_4iZ4jHwPr-6"

URL = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

payload = {
    "ietf-interfaces:interfaces": {
        "interface": [
            {
                "name": "GigabitEthernet2",
                "description": "Updated: Configured by yours truly, iBroughtWinRAR"
            }
        ]
    }
}

response = requests.patch(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, json=payload, verify=False)

print(f"Status Code: [{response.status_code}]")

if response.text:
    print(f"Response: {json.dumps(response.json(), indent=4)}")
else:
    print("No response body — change applied successfully.")




