from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

@app.route("/upload")
def upload():
    try:
        account_url = "https://stfunstagram01.blob.core.windows.net"
        container_name = "images"

        credential = DefaultAzureCredential()
        blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

        blob_client = blob_service_client.get_blob_client(container=container_name, blob="test.txt")

        data = "Hello from Funstagram 🚀"

        blob_client.upload_blob(data, overwrite=True)

        return "File uploaded successfully ✅"

    except Exception as e:
        return f"Upload failed: {str(e)}"
