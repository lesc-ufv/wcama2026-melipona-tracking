# Tracking Melipona capixaba Bees using Computer Vision

This repository contains the source code, configurations, models, and validation data used in the paper **"Tracking Melipona capixaba Bees using Computer Vision"**, accepted at **WCAMA 2026**.

## 📌 About the Project
Non-invasive monitoring of the *Melipona capixaba* (an endemic and endangered species) is an essential tool for ecological conservation and the advancement of Precision Meliponiculture. This work proposes a computer vision pipeline, evaluating the technological trade-off between Transformer-based models (RT-DETR) and convolutional networks (YOLO11n, YOLO26n) under quantization, integrated with the **ByteTrack** algorithm for multi-object tracking (MOT).

## 📂 Repository Structure

```text
wcama2026-melipona-tracking/
├── bee_dataset_mot/
│   └── gt/
│       ├── gt.txt                                 # Ground Truth file for the MOT test
│       └── labels.txt                             # Class identification labels
├── configs/
│   ├── hyp.yaml                                   # YOLO networks training hyperparameters (AdamW, lr, etc.)
│   └── hyp_rtdetr.yaml                            # RT-DETR specific training hyperparameters
├── dataset/                                       # Target directory for the dataset (populated via script)
├── modelos/                                       # Target directory for pre-trained weights (populated via script)
├── notebooks/
│   ├── model_testing_pipeline.ipynb               # Notebook containing the models' testing pipeline
│   ├── training_rt_detr.ipynb                     # Notebook containing the RT-DETR training pipeline
│   ├── training_yolo11n.ipynb                     # Notebook containing the YOLO11n training pipeline
│   └── training_yolo26n.ipynb                     # Notebook containing the YOLO26n training pipeline
├── test_mot/
│   ├── first_frame_roi.jpg                        # Reference image for defining the counting ROI
│   ├── full_video_2025_12_12_h15_M04_S54.mkv      # Complete field recording
│   └── test_10_seconds.mp4                        # 10s video clip used for MOTA/IDF1 validation
├── CITATION.cff                                   # Citation metadata file
├── README.md                                      # Repository documentation
├── README.pt-br.md                                # Repository documentation in Portuguese
└── setup_assets.py                                # Automated script to download large files

```

## 🚀 How to Set Up the Environment

Because the exported models and the raw dataset exceed standard GitHub storage limits, the repository uses the `setup_assets.py` script to automatically fetch the compressed files directly from Google Drive.

### 1. Automated Data and Model Download

At the root of the project, run the automation script:

```bash
python setup_assets.py

```

This script will create the necessary folders and perform the download/extraction of:

* **Dataset:** The complete dataset containing images structured in YOLO format (`dataset/`).
* **Models:** The compressed weights files (`modelos/`).

## 📊 Reproducing the Paper's Metrics

1. **Practical Validation and MOTA:** The analytical data for the temporal consistency and directional flow test (mentioned in Section 5.2 of the paper) directly use the files contained in the `/test_mot` and `/bee_dataset_mot/gt/gt.txt` folders.
2. **Hyperparameters:** The files in the `/configs` folder detail the initial learning rate (lr0 = 0.001667), AdamW optimizer, loss gains, and in-memory geometric transformations used to mitigate class imbalance from the real-world scenario.
3. **Training:** The notebooks in `/notebooks` document the end-to-end training process and the convergence curves obtained on the GPU before the INT8 quantization process for the edge.
4. **Hive entrance:** ROI = {"xmin": 415, "ymin": 415, "xmax": 540, "ymax": 580}

## ✒️ Author

* **Marcos Veniciu de Sá Barbalho** - Researcher and Developer (Master's focusing on systems architecture and non-invasive ecological monitoring).


## 📄 Citation

If you use this dataset, models, or code in your research, please cite both the original paper and the Zenodo repository:

**Original Article (WCAMA 2026):**
> de Sá Barbalho, M. V., Matos, T. N., Gomes, I., Ferreira, R. S., Resende, H. C., & Nacif, J. A. M. (2026). Rastreamento de Abelhas da Espécie Melipona capixaba utilizando Visão Computacional. *Anais do Workshop de Computação Aplicada à Gestão do Meio Ambiente e Recursos Naturais (WCAMA)*.

**Dataset & Models (Zenodo):**
> de Sá Barbalho, M. V. et al. (2026). Dataset and Models - Tracking Melipona capixaba Bees using Computer Vision (Version 1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.20276311