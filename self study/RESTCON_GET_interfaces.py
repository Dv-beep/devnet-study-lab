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

response = requests.get(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

print(f"Status Code: [{response.status_code}]")

data = response.json()

for interface in data['ietf-interfaces:interfaces']['interface']:
    print(f"Response: {json.dumps(interface, indent=4)}",
    print("------------------------------------------------------------"),
    print("interface name: ", interface['name']),
    print("interface description: ", interface.get('description', 'N/A')),
    print("interface Enabled: ", interface.get('enabled', 'N/A'))
          )

