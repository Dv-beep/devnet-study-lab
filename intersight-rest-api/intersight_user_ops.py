"""
    intersight_user_ops.py - shows how to use intersight REST API

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

if __name__ == "__main__":

    # intersight operations, GET, POST, PATCH, DELETE
    OPERATIONS = [
        {
            "request_process":False,
            "resource_path":"iam/Users",
            "request_method":"POST",
            "request_body": {
                "Email":"person@email.com",
                "Idpreference": {
                    "Selector": "$filter=Name eq 'Cisco'"
                },
                "Permissions": [
                    {
                        "Selector": "$filter=Name eq 'Device Administrator'"
                    },
                    {
                        "Selector": "$filter=Name eq 'HyperFlex Cluster Administrator'"
                    }
                ]
            }
        },
        {
            "request_process":False,
            "resource_name":"person@email.com",
            "resource_path":"iam/Users",
            "request_method":"PATCH",
            "request_body":{
                "Permissions": [
                    {
                        "Selector": "$filter=Name eq 'Device Administrator'"
                    }
                ]
            }
        },
        {
            "request_process":False,
            "resource_name":"person@email.com",
            "resource_path":"iam/Users",
            "request_method":"DELETE"
        }
    ]


    for operation in OPERATIONS:

        if operation['request_process']:

            response = None
            resource_path = str(operation['resource_path'])
            method = str(operation['request_method'])
            print(method)

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
                    BURL + resource_path + "?$filter=Email eq '" + resource_name + "'",
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
                    BURL + resource_path + "?$filter=Email eq '" + resource_name + "'",
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
