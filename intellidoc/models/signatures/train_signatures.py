from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # modelo base
model.train(data='datasets/signature.yaml', epochs=30, imgsz=640)
