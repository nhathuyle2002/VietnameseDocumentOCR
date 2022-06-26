import os
import cv2
from modules import Preprocess, Detection, OCR, Correction
from tool.utils import natural_keys
import matplotlib.pyplot as plt

def img_to_txt(path):
    # Read image
    img_id = 'test'
    img = cv2.imread(path)

    # Initialize modules
    det_model = Detection(weight_path='weights/PANNet_best_map.pth')
    ocr_model = OCR(weight_path='weights/transformerocr.pth')
    preproc = Preprocess(
        det_model=det_model,
        ocr_model=ocr_model,
        find_best_rotation=False)
    correction = Correction()

    # Preprocess image
    img1 = preproc(img)

    # Detect texts
    boxes, img2  = det_model(
        img1,
        crop_region=True,                               #Crop detected regions for OCR
        return_result=True,                             # Return plotted result
        output_path=f"results\{img_id}"   #Path to save cropped regions
    )

    # Text OCR
    img_paths=os.listdir(f"results\{img_id}\crops") # Cropped regions
    img_paths.sort(key=natural_keys)
    img_paths = [os.path.join(f"results\{img_id}\crops", i) for i in img_paths]

    texts, probs = ocr_model.predict_folder(img_paths, return_probs=True) # OCR
    texts = correction(texts)   # Word correction

    # for i in texts:
    #     print(i)

    return ' '.join(texts)

