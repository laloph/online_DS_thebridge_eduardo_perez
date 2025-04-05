# utils.py
import os
import requests

def download_from_gdrive(file_id, destination_path):
    """
    Descarga un archivo desde Google Drive dado su ID y lo guarda localmente.
    
    Parámetros:
    - file_id: str. ID del archivo en Google Drive.
    - destination_path: str. Ruta local donde se guardará el archivo.
    """
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    print(f"⬇️ Descargando desde Google Drive a: {destination_path} ...")

    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(destination_path, "wb") as f:
            for chunk in response.iter_content(32768):
                f.write(chunk)
        print(f"✅ Archivo guardado como: {destination_path}")
    else:
        print(f"❌ Error al descargar el archivo. Código HTTP: {response.status_code}")
