#!/Users/dan/workspace/venv/fing-scan/bin/python

import sys, requests, json, os
from mac_address import MacAddr

mac = sys.argv[1]
action = sys.argv[2]
device = MacAddr[mac] if MacAddr.has_key(mac) else "Unknown Device({})".format(mac)
color = "good" if action == "online" else "warning"

slack_token = os.environ["HUGINN_FING_URL"]
payload = {'color': color, 'device': device, 'action': action}
requests.post(url, json = payload)
