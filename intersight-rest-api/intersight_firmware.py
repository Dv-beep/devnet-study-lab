"""
    intersight_firmware.py - shows how to use intersight REST API
                             to initiate a firmware upgrade.

    author: John McDonough (jomcdono@cisco.com)
"""
# pylint: disable=line-too-long,invalid-name

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

    # Intersight REST API Operations
    rackunit_json_body = {
        "request_method":"GET",
        "resource_path": (
            'https://www.intersight.com/api/v1/'+
            'compute/RackUnits?$select=DeviceMoId,Model,AssetTag&'+
            '$filter=AssetTag eq \'DMZ-R-L3-ADJM\''
        )
    }
    firmware_json_body = {
        "request_method":"POST",
        "resource_path":"https://www.intersight.com/api/v1/firmware/Upgrades",
        "request_body":{
            "DirectDownload":{},
            "NetworkShare":{
                "MapType":"www",
                "Upgradeoption":"nw_upgrade_full",
                "HttpServer":{
                    "LocationLink": "http://cloud-city-gateway.eastus.cloudapp.azure.com/ucs-c240m4-huu-4.0.2h.iso"
                }
            },
            "UpgradeType":"network_upgrade",
            "Server":""
        }
    }

    RESPONSE = requests.request(
        method=str(rackunit_json_body['request_method']),
        url=str(rackunit_json_body['resource_path']),
        auth=AUTH
    )
    print(RESPONSE)
    print(RESPONSE.text)

    request_body = dict(firmware_json_body['request_body'])  # type: ignore[arg-type]
    request_body['Server'] = json.loads(RESPONSE.text)['Results'][0]['Moid']

    print(request_body)

    RESPONSE = requests.request(
        method=str(firmware_json_body['request_method']),
        url=str(firmware_json_body['resource_path']),
        data=json.dumps(request_body),
        auth=AUTH
    )

    print(RESPONSE)
    print(RESPONSE.text)
