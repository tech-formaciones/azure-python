from blobs import *

# Conexión al servicio de Blob Storage
connection_string = "DefaultEndpointsProtocol=https;AccountName=<your_account_name>;AccountKey=<your_account_key>;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)


# Listar todos los contenedores
print("Listado de Contenedores:")
list_containers(blob_service_client)

# Listar blobs en un contenedor específico
container_name = "<your_container_name>"
list_blobs(container_name)

# Descargar un blob específico
blob_name = "<your_blob_name>"
download_file_path = os.path.join(os.getcwd(), blob_name)
download_blob(container_name, blob_name, download_file_path)