import os
import zipfile
import requests

# ==========================================
# CONFIGURAÇÃO DO ZENODO
# ==========================================
ZENODO_RECORD_ID = "20276311"

URLS = {
    "dataset": f"https://zenodo.org/records/{ZENODO_RECORD_ID}/files/dataset_abelhas_v3.zip?download=1",
    "modelos": f"https://zenodo.org/records/{ZENODO_RECORD_ID}/files/modelos.zip?download=1"
}

def criar_diretorios():
    """Cria os diretórios raiz base para o projeto."""
    pastas = ['dataset', 'modelos']
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"Diretório raiz '{pasta}/' criado.")

def baixar_do_zenodo(url, destino):
    """Faz o download do arquivo via stream para não sobrecarregar a RAM."""
    print(f"\n📥 Baixando {os.path.basename(destino)} do Zenodo...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(destino, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Download de {os.path.basename(destino)} concluído.")
        return True
    except Exception as e:
        print(f"Erro ao baixar {os.path.basename(destino)}. Detalhes: {e}")
        return False

def extrair_zip(caminho_zip, pasta_destino):
    """Extrai o conteúdo do ZIP para a pasta especificada."""
    if os.path.exists(caminho_zip):
        print(f"📦 Extraindo {os.path.basename(caminho_zip)} para '{pasta_destino}'...")
        try:
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
            print(f"✅ Extração de {os.path.basename(caminho_zip)} concluída.")
            return True
        except zipfile.BadZipFile:
            print(f"❌ Erro: Arquivo {caminho_zip} parece estar corrompido.")
            return False
    else:
        print(f"Arquivo {caminho_zip} não encontrado para extração.")
        return False

if __name__ == "__main__":
    print("Iniciando configuração do ambiente de testes via Zenodo...")
    
    if ZENODO_RECORD_ID == "SEU_RECORD_ID_AQUI":
        print("ATENÇÃO: Você precisa alterar a variável 'ZENODO_RECORD_ID' no código com o ID da sua publicação no Zenodo.")
        exit(1)

    criar_diretorios()
    
    # Caminhos temporários para os zips principais
    caminho_dataset_zip = "dataset/dataset_abelhas_v3.zip"
    caminho_modelos_zip = "modelos/modelos.zip"
    
    # 1. Realizar os Downloads
    download_dataset = baixar_do_zenodo(URLS["dataset"], caminho_dataset_zip)
    download_modelos = baixar_do_zenodo(URLS["modelos"], caminho_modelos_zip)
    
    if not (download_dataset and download_modelos):
        print("\nFalha nos downloads. Verifique seu ZENODO_RECORD_ID e a conexão de rede.")
        exit(1)
        
    print("\nIniciando descompactação e estruturação de pastas...")
    
    # 2. Processar o Dataset
    extrair_zip(caminho_dataset_zip, "dataset/")
    if os.path.exists(caminho_dataset_zip):
        os.remove(caminho_dataset_zip) # Limpeza
        
    # 3. Processar os Modelos
    # Primeiro, extraímos o master zip que contém os 3 zips das arquiteturas
    if extrair_zip(caminho_modelos_zip, "modelos/"):
        
        # Mapeamento: "Nome do zip interno" -> "Subpasta onde ele deve ser extraído"
        estruturas_arquiteturas = {
            "modelos/rt_dert_exportados_rpi5.zip": "modelos/rtdetr",
            "modelos/yolo_11n_exportados_rpi5.zip": "modelos/yolo11n",
            "modelos/yolo_26n_exportados_rpi5.zip": "modelos/yolo26n"
        }
        
        print("\nCriando subdiretórios individuais para cada arquitetura...")
        
        for caminho_zip_interno, pasta_destino in estruturas_arquiteturas.items():
            # Cria a subpasta específica (ex: modelos/rtdetr)
            os.makedirs(pasta_destino, exist_ok=True)
            
            # Extrai o zip interno para dentro da subpasta correspondente
            if extrair_zip(caminho_zip_interno, pasta_destino):
                # Limpa o zip interno após extrair com sucesso
                if os.path.exists(caminho_zip_interno):
                    os.remove(caminho_zip_interno)
                    
        # Limpa o zip principal (modelos.zip)
        if os.path.exists(caminho_modelos_zip):
            os.remove(caminho_modelos_zip)
            
    print("\nAmbiente 100% configurado!")
    print("A árvore de arquivos está idêntica à especificada, pronta para o rastreamento das abelhas.")