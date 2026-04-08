from flask import Flask
import os
from applicationinsights import TelemetryClient

app = Flask(__name__)

instrumentation_key = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")

tc = None
if instrumentation_key:
    tc = TelemetryClient(instrumentation_key)

@app.route("/")
def home():
    return "Welcome to Funstagram 🚀"

@app.route("/break")
def break_app():
    try:
        return 1/0
    except Exception:
        if tc:
            tc.track_exception()
            tc.flush()
        return "Error triggered"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
