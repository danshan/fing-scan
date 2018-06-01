#!/Users/dan/workspace/venv/fing-scan/bin/python

import sys 
from slackclient import SlackClient
from mac_address import MacAddr

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

mac = sys.argv[1]
action = sys.argv[2]
device = MacAddr[mac] if MacAddr.has_key(mac) else "Unknown Device({})".format(mac)
color = "good" if action == "online" else "warning"

sc.api_call(
  "chat.postMessage",
  channel="debug",
  attachments=[{"text": "{} `{}`".format(device, action), "color": color}]
)

