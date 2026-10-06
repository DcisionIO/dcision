"""Usage: DCISION_API_KEY=dcs_live_... python run_decision.py [slug]  (standard library only)"""
import json
import os
import sys
import urllib.error
import urllib.request

slug = sys.argv[1] if len(sys.argv) > 1 else "lead-qualification"
state = {
    "message": "We need pricing for 500 users and want to start next month.",
    "company_size": 500,
    "source": "website",
}
request = urllib.request.Request(
    f"https://api.dcision.io/v1/decisions/{slug}",
    data=json.dumps({"state": state}).encode(),
    headers={"Authorization": f"Bearer {os.environ['DCISION_API_KEY']}", "Content-Type": "application/json"},
    method="POST",
)
try:
    with urllib.request.urlopen(request, timeout=10) as response:
        decision = json.load(response)
except urllib.error.HTTPError as error:
    body = json.load(error)
    raise SystemExit(f"{body['error']['code']}: {body['error']['message']}")

# Route on the typed answer and the action — no text to parse.
print(decision["action"], decision["result"], decision["confidence"])
