# Rastreamento de Abelhas da Espécie Melipona capixaba utilizando Visão Computacional

Este repositório contém o código-fonte, as configurações, os modelos e os dados de validação utilizados no artigo **"Rastreamento de Abelhas da Espécie Melipona capixaba utilizando Visão Computacional"**, aceito no **WCAMA 2026**.

## 📌 Sobre o Projeto
O monitoramento não invasivo da *Melipona capixaba* (espécie endêmica e em perigo de extinção) é uma ferramenta essencial para a conservação ecológica e o avanço da Meliponicultura de Precisão. Este trabalho propõe um pipeline de visão computacional, avaliando o *trade-off* tecnológico entre modelos baseados em Transformers (RT-DETR) e redes convolucionais (YOLO11n, YOLO26n) sob quantização, integrados ao algoritmo **ByteTrack** para rastreamento multi-alvos (MOT).

## 📂 Estrutura do Repositório

```text
wcama2026-melipona-tracking/
├── bee_dataset_mot/
│   └── gt/
│       ├── gt.txt                                 # Arquivo de Ground Truth para o teste MOT
│       └── labels.txt                             # Rótulos de identificação das classes
├── configs/
│   ├── hyp.yaml                                   # Hiperparâmetros de treino das redes YOLO (AdamW, lr, etc.)
│   └── hyp_rtdetr.yaml                            # Hiperparâmetros de treino específicos do RT-DETR
├── dataset/                                       # Diretório destino do dataset (populado via script)
├── modelos/                                       # Diretório destino dos pesos pré-treinados (populado via script)
├── notebooks/
│   ├── model_testing_pipeline.ipynb               # Notebook contendo o pipeline de teste dos modelos
│   ├── training_rt_detr.ipynb                     # Notebook contendo o pipeline de treino do RT-DETR
│   ├── training_yolo11n.ipynb                     # Notebook contendo o pipeline de treino do YOLO11n
│   └── training_yolo26n.ipynb                     # Notebook contendo o pipeline de treino do YOLO26n
├── test_mot/
│   ├── first_frame_roi.jpg                        # Imagem de referência para definição da ROI de contagem
│   ├── full_video_2025_12_12_h15_M04_S54.mkv      # Registro completo de campo
│   └── test_10_seconds.mp4                        # Recorte de vídeo de 10s usado na validação do MOTA/IDF1
├── CITATION.cff                                   # Arquivo de metadados de citação
├── README.md                                      # Documentação do repositório
├── README.pt-br.md                                # Documentação do repositório em Português
└── setup_assets.py                                # Script automatizado para download de arquivos pesados

```

## 🚀 Como Configurar o Ambiente

Como os modelos exportados e o conjunto de dados bruto ultrapassam os limites de armazenamento padrão do GitHub, o repositório utiliza o script `setup_assets.py` para buscar os arquivos compactados diretamente do Google Drive de forma automatizada.

### 1. Download Automatizado de Dados e Modelos

Na raiz do projeto, execute o script de automação:

```bash
python setup_assets.py

```

Este script irá criar as pastas necessárias e realizar o download/extração de:

* **Dataset:** O conjunto de dados completo contendo as imagens estruturadas em formato YOLO (`dataset/`).
* **Modelos:** Os arquivos de pesos compactados (`modelos/`).

## 📊 Reproduzindo as Métricas do Artigo

1. **Validação Prática e MOTA:** Os dados analíticos do teste de consistência temporal e fluxo direcional (mencionados na Seção 5.2 do artigo) utilizam diretamente os arquivos contidos na pasta `/test_mot` e `/bee_dataset_mot/gt/gt.txt`.
2. **Hiperparâmetros:** Os arquivos na pasta `/configs` detalham a taxa de aprendizado inicial ($lr0 = 0.001667$), otimizador AdamW, e os ganhos de perda e transformações geométricas na memória utilizados para mitigar o desbalanceamento de classes do cenário real.
3. **Treinamento:** Os notebooks em `/notebooks` documentam de ponta a ponta o processo de treinamento e as curvas de convergência obtidas na GPU antes do processo de quantização INT8 para a borda.
4. **Entrada da colmeia:** ROI = {"xmin": 415, "ymin": 415, "xmax": 540, "ymax": 580}

## ✒️ Autor

* **Marcos Veniciu de Sá Barbalho** - Pesquisador e Desenvolvedor (Mestrado focado em arquitetura de sistemas e monitoramento ecológico não invasivo).

## 📄 Citação

Se você utilizar este conjunto de dados, modelos ou código em sua pesquisa, por favor cite o artigo original e o repositório no Zenodo:

**Artigo Original (WCAMA 2026):**
> de Sá Barbalho, M. V., Matos, T. N., Gomes, I., Ferreira, R. S., Resende, H. C., & Nacif, J. A. M. (2026). Rastreamento de Abelhas da Espécie Melipona capixaba utilizando Visão Computacional. *Anais do Workshop de Computação Aplicada à Gestão do Meio Ambiente e Recursos Naturais (WCAMA)*.

**Dataset e Modelos (Zenodo):**
> de Sá Barbalho, M. V. et al. (2026). Dataset e Modelos - Rastreamento de Abelhas da Espécie Melipona capixaba utilizando Visão Computacional (Versão 1.0.0) [Conjunto de dados]. Zenodo. https://doi.org/10.5281/zenodo.20276311