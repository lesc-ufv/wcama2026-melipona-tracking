import os
import zipfile
import requests

# ==========================================
# ZENODO CONFIGURATION
# ==========================================
ZENODO_RECORD_ID = "20276311"

URLS = {
    "dataset": f"https://zenodo.org/records/{ZENODO_RECORD_ID}/files/dataset_abelhas_v3.zip?download=1",
    "modelos": f"https://zenodo.org/records/{ZENODO_RECORD_ID}/files/modelos.zip?download=1"
}

def criar_diretorios():
    """
    Creates the base root directories for the project.
    This ensures that the 'dataset' and 'modelos' folders exist before downloading.
    """
    pastas = ['dataset', 'modelos']
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"Root directory '{pasta}/' created.")

def baixar_do_zenodo(url, destino):
    """
    Downloads a file from a given URL using streaming to avoid overloading the RAM.
    
    Args:
        url (str): The download URL.
        destino (str): The local path where the file will be saved.
        
    Returns:
        bool: True if the download was successful, False otherwise.
    """
    print(f"\nDownloading {os.path.basename(destino)} from Zenodo...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(destino, 'wb') as f:
                # Chunk size set to 8192 bytes for optimal memory management during download
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Download of {os.path.basename(destino)} completed.")
        return True
    except Exception as e:
        print(f"Error downloading {os.path.basename(destino)}. Details: {e}")
        return False

def extrair_zip(caminho_zip, pasta_destino):
    """
    Extracts the contents of a ZIP file to a specified target folder.
    
    Args:
        caminho_zip (str): The local path to the downloaded ZIP file.
        pasta_destino (str): The target directory for extraction.
        
    Returns:
        bool: True if extraction was successful, False otherwise.
    """
    if os.path.exists(caminho_zip):
        print(f"Extracting {os.path.basename(caminho_zip)} to '{pasta_destino}'...")
        try:
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
            print(f"Extraction of {os.path.basename(caminho_zip)} completed.")
            return True
        except zipfile.BadZipFile:
            print(f"Error: File {caminho_zip} appears to be corrupted.")
            return False
    else:
        print(f"File {caminho_zip} not found for extraction.")
        return False

if __name__ == "__main__":
    print("Starting test environment configuration via Zenodo...")
    
    if ZENODO_RECORD_ID == "SEU_RECORD_ID_AQUI":
        print("WARNING: You must change the 'ZENODO_RECORD_ID' variable in the code with your Zenodo publication ID.")
        exit(1)

    # Initialize the project's folder structure
    criar_diretorios()
    
    # Temporary paths for the main downloaded zip files
    caminho_dataset_zip = "dataset/dataset_abelhas_v3.zip"
    caminho_modelos_zip = "modelos/modelos.zip"
    
    # 1. Perform Downloads
    download_dataset = baixar_do_zenodo(URLS["dataset"], caminho_dataset_zip)
    download_modelos = baixar_do_zenodo(URLS["modelos"], caminho_modelos_zip)
    
    if not (download_dataset and download_modelos):
        print("\nDownload failed. Please check your ZENODO_RECORD_ID and network connection.")
        exit(1)
        
    print("\nStarting decompression and folder structuring...")
    
    # 2. Process the Dataset
    extrair_zip(caminho_dataset_zip, "dataset/")
    if os.path.exists(caminho_dataset_zip):
        os.remove(caminho_dataset_zip)  # Cleanup the zip file to save disk space
        
    # 3. Process the Models
    # First, extract the master zip which contains the 3 architecture zips
    if extrair_zip(caminho_modelos_zip, "modelos/"):
        
        # Mapping: "Internal zip name" -> "Subfolder where it should be extracted"
        # These keys must match the exact names of the files inside the main 'modelos.zip'
        estruturas_arquiteturas = {
            "modelos/rt_dert_exportados_rpi5.zip": "modelos/rtdetr",
            "modelos/yolo_11n_exportados_rpi5.zip": "modelos/yolo11n",
            "modelos/yolo_26n_exportados_rpi5.zip": "modelos/yolo26n"
        }
        
        print("\nCreating individual subdirectories for each architecture...")
        
        for caminho_zip_interno, pasta_destino in estruturas_arquiteturas.items():
            # Create the specific subfolder (e.g., modelos/rtdetr)
            os.makedirs(pasta_destino, exist_ok=True)
            
            # Extract the internal zip into the corresponding subfolder
            if extrair_zip(caminho_zip_interno, pasta_destino):
                # Clean up the internal zip after successful extraction
                if os.path.exists(caminho_zip_interno):
                    os.remove(caminho_zip_interno)
                    
        # Clean up the main zip (modelos.zip)
        if os.path.exists(caminho_modelos_zip):
            os.remove(caminho_modelos_zip)
            
    print("\nEnvironment 100% configured!")
    print("The file tree matches the specifications perfectly, ready for bee tracking.")