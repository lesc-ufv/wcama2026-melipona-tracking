import os
import zipfile
import gdown

# Substitua pelos seus links reais de compartilhamento do Google Drive
URLS = {
    "dataset": "https://drive.google.com/file/d/1cDSHL7_WyG11Ax0i1lExyD0Q9tDGUV1W/view?usp=drive_link",
    "yolo11n": "https://drive.google.com/file/d/1GLv27baYNQceOUlkSpKYBI3R8Sl-zwyB/view?usp=drive_link",
    "yolo26n": "https://drive.google.com/file/d/1M4RXSupisR9Nv9U6KkkyBLofGZPEslXl/view?usp=drive_link",
    "rtdetr": "https://drive.google.com/file/d/16MIWvF_hpvOSbW-dssrRm33Xq6N6knf_/view?usp=drive_link"
}

def criar_diretorios():
    """Cria a estrutura de pastas necessária se não existirem."""
    pastas = ['dataset', 'modelos']
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"📁 Diretório '{pasta}/' criado com sucesso.")

def baixar_arquivo_gdrive(url, destino):
    """Realiza o download de um arquivo do Google Drive usando gdown."""
    print(f"\n📥 Baixando {os.path.basename(destino)}...")
    try:
        # fuzzy=True permite usar o link padrão de compartilhamento do Drive
        gdown.download(url, destino, quiet=False, fuzzy=True)
        print(f"✅ Download de {os.path.basename(destino)} concluído.")
        return True
    except Exception as e:
        print(f"❌ Erro ao baixar {os.path.basename(destino)}. Erro: {e}")
        return False

def extrair_zip(caminho_zip, pasta_destino):
    """Extrai um arquivo ZIP na pasta de destino informada."""
    if os.path.exists(caminho_zip):
        print(f"📦 Extraindo {os.path.basename(caminho_zip)} em '{pasta_destino}'...")
        try:
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
            print(f"✅ Extração de {os.path.basename(caminho_zip)} concluída!")
            # Opcional: descomente a linha abaixo se quiser apagar o .zip após extrair para poupar espaço no RPi5
            # os.remove(caminho_zip)
        except zipfile.BadZipFile:
            print(f"❌ Erro: O arquivo {caminho_zip} parece estar corrompido ou não é um ZIP válido.")
    else:
        print(f"⚠️ Arquivo {caminho_zip} não encontrado para extração.")

if __name__ == "__main__":
    print("🚀 Iniciando configuração do ambiente de testes para Raspberry Pi 5...")
    criar_diretorios()
    
    # Definição dos caminhos locais com os novos nomes de arquivos
    caminhos = {
        "dataset": "dataset/dataset_abelhas_v3.zip",
        "yolo11n": "modelos/yolo_11n_exportados_rpi5.zip",
        "yolo26n": "modelos/yolo_26n_exportados_rpi5.zip",
        "rtdetr": "modelos/rt_dert_exportados_rpi5.zip"
    }
    
    # Executa os downloads
    downloads_ok = True
    for chave, url in URLS.items():
        if not baixar_arquivo_gdrive(url, caminhos[chave]):
            downloads_ok = False
    
    # Se algum download falhar, avisa o usuário antes de tentar extrair
    if not downloads_ok:
        print("\n⚠️ Alguns downloads falharam. Verifique os links do Google Drive e tente novamente.")
    
    print("\n📦 Iniciando a extração dos arquivos...")
    # Extrai o dataset na pasta 'dataset/'
    extrair_zip(caminhos["dataset"], "dataset/")
    
    # Extrai os modelos na pasta 'modelos/'
    extrair_zip(caminhos["yolo11n"], "modelos/")
    extrair_zip(caminhos["yolo26n"], "modelos/")
    extrair_zip(caminhos["rtdetr"], "modelos/")
    
    print("\n🎉 Ambiente configurado e pronto para os testes no Raspberry Pi 5!")