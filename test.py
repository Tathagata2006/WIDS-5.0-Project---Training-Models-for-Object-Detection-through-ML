
#Testing on testimages
from ultralytics import YOLO

model = YOLO("runs/detect/choco_run/weights/best.pt")
model.predict(r"D:\WIDS 5.0 Object\test_images\13.jpg", conf=0.25, save=True)
