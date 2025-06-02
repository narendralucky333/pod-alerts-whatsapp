from flask import Flask, request
import requests

app = Flask(__name__)

recipients = [
    {"phone": "+919989774167", "apikey": "abc123xyz"}
]

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    data = request.json
    alerts = data.get('alerts', [])
    for alert in alerts:
        message = f"[{alert['status'].upper()}] {alert['labels'].get('alertname')}:\n{alert['annotations'].get('description')}"
        for recipient in recipients:
            phone = recipient["phone"]
            apikey = recipient["apikey"]
            url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={message}&apikey={apikey}"
            requests.get(url)
    return "Sent", 200
