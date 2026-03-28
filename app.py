from flask import Flask
import requests   # 👈 ADD THIS

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Funstagram 🚀"

@app.route("/about")
def about():
    return "Built by DevOps Engineer"

@app.route("/internal")
def internal():
    return requests.get("http://10.0.2.4").text   # 👈 your VM private IP

if __name__ == "__main__":
    app.run()
