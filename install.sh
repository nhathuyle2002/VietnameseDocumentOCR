pip install -r requirements.txt
pip install pandas torch scipy pylsd lsd ocrd-fork-pylsd==0.0.3 torchvision pyyaml tqdm sklearn pycocotools Polygon pyclipper scikit-image einops
pip install gdown==4.4.0 webcolors transformers
gdown --fuzzy 'https://drive.google.com/uc?id=1-Nj8TSM_eqZDZzRArZjWPcVCtl1l2uQP' -O '/weights/PANNet_best_map.pth'
gdown --fuzzy 'https://drive.google.com/uc?id=1qpXp_-digz2HPTGY_GPdwstzGLhjC_ot' -O '/weights/transformerocr.pth'
## --> Run file main.py