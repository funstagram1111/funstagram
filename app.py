from flask import Flask
import requests
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

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
        response = requests.get("http://10.0.2.4")  # 🔁 replace with your VM private IP
        return response.text
    except Exception as e:
        return f"Internal call failed: {str(e)}"

@app.route("/secret")
def get_secret():
    try:
        kv_url =  "https://kv-funstagram-01.vault.azure.net/" # 🔁 replace

        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=kv_url, credential=credential)

        secret = client.get_secret("db-password")

        # Secure usage (not exposing value)
        if secret.value:
            return "Secret accessed securely ✅"
        else:
            return "Secret not found"

    except Exception as e:
        return f"Error fetching secret: {str(e)}"

# IMPORTANT for Azure
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
