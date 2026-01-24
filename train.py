#Training on dataset

from ultralytics import YOLO

model = YOLO("yolov8n.pt")   # you have yolov8n.pt in same folder

model.train(
    data="choco_dataset/data.yaml",
    epochs=80,
    imgsz=640,
    batch=8,
    name  = 'choco_run'
)
