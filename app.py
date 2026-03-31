from flask import Flask
from applicationinsights import TelemetryClient
import requests
import os


app = Flask(__name__)

instrumentation_key = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")
tc = TelemetryClient(instrumentation_key)


@app.route("/")
def home():
     tc.tract_event("HomePageVisited")
     tc.flush()
     return "Welcome to Funstagram"

@app.route("/about")
def about():
    return "Built by DevOps Engineer"


@app.route("/")
def home():
    tc.track_event("HomePageVisited")
    tc.flush()
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
        return f"Error: {str(e)}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
