from flask import Flask
import requests
import os
from applicationinsights import TelemetryClient

app = Flask(__name__)

instrumentation_key = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")
tc = TelemetryClient(instrumentation_key)

@app.route("/")
def home():
    tc.track_event("HomePageVisited")
    tc.flush()
retrun 1/0
    return "Welcome to Funstagram 🚀"

@app.route("/secret")
def get_secret():
    try:
        secret = os.environ.get("DB_PASSWORD")

        tc.track_event("SecretAccessed")
        tc.flush()

        if secret:
            return "Secret accessed via env ✅"
        else:
            return "Secret not found"
    except Exception as e:
        tc.track_exception()
        tc.flush()
        return "Error occurred"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
