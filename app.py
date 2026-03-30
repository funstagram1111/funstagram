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

@app.route("/internal")
def internal():
    try:
        response = requests.get("http://10.1.x.x", timeout=2)
        return response.text
    except Exception as e:
        return f"Internal call failed: {str(e)}"

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

if__name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
