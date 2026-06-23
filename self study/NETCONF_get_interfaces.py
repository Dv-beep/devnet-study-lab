from ncclient import manager
from xml.dom import minidom

HOST = "devnetsandboxiosxec8k.cisco.com"
USER = "christiantech03"
PASS = "TYx_a38GiE8_"

filter = ('subtree', '<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>')

with manager.connect(  # type: ignore[union-attr]
    host=HOST,
    port=830,
    username=USER,
    password=PASS,
    hostkey_verify=False,
    look_for_keys=False
) as m:
    xml_pretty = minidom.parseString(m.get_config(source="running").xml).toprettyxml()
    print(xml_pretty)

    reply = m.get(filter=filter)
    print(minidom.parseString(reply.xml).toprettyxml())