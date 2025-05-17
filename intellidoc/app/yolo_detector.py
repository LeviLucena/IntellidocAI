# app/yolo_detector.py

import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont
import io
import numpy as np
import base64
from ultralytics import YOLO

# Carrega o modelo YOLOv8
model = YOLO('yolov8n.pt')

def convert_page_to_image(page, dpi=150):
    pix = page.get_pixmap(dpi=dpi)
    return Image.open(io.BytesIO(pix.tobytes("png")))

def detect_visual_elements(file_stream):
    """
    Detecta elementos visuais com YOLOv8 em cada página de um PDF.
    Retorna uma lista de dicionários com detecções por página.
    """
    detections = []
    doc = fitz.open(stream=file_stream.read(), filetype="pdf")

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        img = convert_page_to_image(page).convert("RGB")
        img_np = np.array(img)

        result = model.predict(img_np, verbose=False)[0]
        page_detections = []

        for box in result.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            page_detections.append({
                'page': page_num + 1,
                'label': label,
                'confidence': round(conf, 2),
                'bbox': [round(x1), round(y1), round(x2), round(y2)]
            })

        detections.append(page_detections)

    return detections

def detect_and_draw(file_stream):
    """
    Aplica YOLO em cada página e retorna imagens com bounding boxes desenhadas (em base64).
    """
    doc = fitz.open(stream=file_stream.read(), filetype="pdf")
    results = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        img = convert_page_to_image(page).convert("RGB")
        img_np = np.array(img)

        detections = model.predict(img_np, verbose=False)[0]

        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()

        for box in detections.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
            draw.text((x1, y1 - 10), f"{label} {conf:.2f}", fill="red", font=font)

        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        results.append(img_base64)

    return results
