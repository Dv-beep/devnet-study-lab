"""
    intersight_ops.py - shows how to use intersight REST API

    author: John McDonough (jomcdono@cisco.com)
"""
import json
import os
import requests
from dotenv import load_dotenv  # type: ignore[import-untyped,import-not-found]

from intersight_auth import IntersightAuth

load_dotenv()

AUTH = IntersightAuth(
    secret_key_filename=os.environ["INTERSIGHT_KEY_FILE"],
    api_key_id=os.environ["INTERSIGHT_API_KEY_ID"]
    )

# Intersight REST API Base URL
BURL = 'https://www.intersight.com/api/v1/'


def _save_json_to_file(obj, filename):
    """Serialize `obj` (a Python structure) to JSON and save under `output/filename`."""
    import os
    os.makedirs('output', exist_ok=True)
    path = os.path.join('output', filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    return path

if __name__ == "__main__":

    # intersight operations, GET, POST, PATCH, DELETE
    OPERATIONS = [
        {
            "request_process":True,
            "resource_path":"compute/PhysicalSummaries",
            "request_method":"GET"
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"GET"
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"POST",
            "request_body":{
                "Enabled":True,
                "Name":"ntp-policy",
                "Description":"NTP Policy for ntp.org",
                "NtpServers":[
                    "pool.ntp.org"
                    ],
                "Tags":[]
            }
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"POST",
            "request_body":{
                "Enabled":True,
                "Name":"ntp-policy-west",
                "Description":"NTP Policy for ntp.org West Coast",
                "NtpServers":[
                    "0.pool.ntp.org",
                    "1.pool.ntp.org"
                    ],
                "Tags":[]
            }
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"POST",
            "request_body":{
                "Enabled":True,
                "Name":"ntp-policy-east",
                "Description":"NTP Policy for ntp.org East Coast",
                "NtpServers":[
                    "2.pool.ntp.org",
                    "3.pool.ntp.org"
                    ],
                "Tags":[]
            }
        },
        {
            "request_process":False,
            "resource_name":"ntp-policy",
            "resource_path":"ntp/Policies",
            "request_method":"PATCH",
            "request_body":{
                "NtpServers":[
                    "pool.ntp.org",
                    "10.10.10.30"
                    ]
                }
        },
        {
            "request_process":False,
            "resource_name":"ntp-policy-east",
            "resource_path":"ntp/Policies",
            "request_method":"DELETE"
        }
    ]


    for operation in OPERATIONS:

        if operation['request_process']:

            response = None
            print(operation['request_method'])

            resource_path = str(operation['resource_path'])
            method = str(operation['request_method'])

            # GET
            if method == "GET":
                response = requests.get(
                    BURL + resource_path,
                    auth=AUTH
                    )

            # POST
            if method == "POST":
                response = requests.post(
                    BURL + resource_path,
                    data=json.dumps(operation['request_body']),
                    auth=AUTH
                    )

            # PATCH
            if method == "PATCH":
                resource_name = str(operation['resource_name'])

                # GET the Moid of the MO to PATCH
                response = requests.get(
                    BURL + resource_path + "?$filter=Name eq '" + resource_name + "'",
                    auth=AUTH
                    )

                # Extract the Moid from the Results
                json_result = json.loads(response.text)
                moid = json_result["Results"][0]["Moid"]

                response = requests.patch(
                    BURL + resource_path + "/" + moid,
                    data=json.dumps(operation['request_body']),
                    auth=AUTH
                    )

            # DELETE
            if method == "DELETE":
                resource_name = str(operation['resource_name'])

                # GET the Moid of the MO to DELETE
                response = requests.get(
                    BURL + resource_path + "?$filter=Name eq '" + resource_name + "'",
                    auth=AUTH
                    )

                # Extract the Moid from the Results
                json_result = json.loads(response.text)
                moid = json_result["Results"][0]["Moid"]

                response = requests.delete(
                    BURL + resource_path + "/" + moid,
                    auth=AUTH
                    )

            assert response is not None
            print(response)
            print(response.text)
            # attempt to parse response body as JSON and save to file
            try:
                parsed = response.json()
                rp = resource_path.replace('/', '_')
                rn = str(operation.get('resource_name', '')).replace(' ', '_')
                filename = f"{method}_{rp}{('_' + rn) if rn else ''}.json"
                saved = _save_json_to_file(parsed, filename)
                print(f"Saved JSON response to: {saved}")
            except ValueError:
                print('Response body is not valid JSON; skipping save')
