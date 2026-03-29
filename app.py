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



from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

@app.route("/secret")
def get_secret():
    kv_url = "https://kv-funstagram-01.vault.azure.net/"
    
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_url, credential=credential)
    
    secret = client.get_secret("db-password")
    return f"Secret value: {secret.value}"
