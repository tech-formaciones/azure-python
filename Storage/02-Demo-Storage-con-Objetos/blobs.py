# Necesitamos instalar la libreria azure.storage.blob
# pip install azure.storage.blob

from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
import os

def list_containers(blob_service_client):
    containers = blob_service_client.list_containers()
    
    for container in containers:
        print(f"- {container['name']}")


def list_blobs(container_name):
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()

    for blob in blobs:
        print(f"  > {blob.name}")


def download_blob(container_name, blob_name, download_file_path):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    
    print(f"Blob '{blob_name}' downloaded to '{download_file_path}'")
