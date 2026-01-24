from ultralytics import YOLO

model = YOLO(r"runs/detect/choco_run/weights/last.pt")
model.train(resume = True)