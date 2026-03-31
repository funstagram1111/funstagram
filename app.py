from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Funstagram 🚀"

@app.route("/about")
def about():
    return "Built by DevOps Engineer"

# Optional (only works if VM exists)
@app.route("/internal")
def internal():
    try:
        response = requests.get("http://10.1.x.x", timeout=2)  # replace if needed
        return response.text
    except Exception as e:
        return f"Internal call failed: {str(e)}"

# Key Vault via environment variable
@app.route("/secret")
def get_secret():
    try:
        secret = os.environ.get("DB_PASSWORD")

        if secret:
            return "Secret accessed via env ✅"
        else:
            return "Secret not found"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
