from ultralytics import YOLO
import glob
import os


model = YOLO("runs/detect/choco_run/weights/best.pt")

test_folder = r"D:\WIDS 5.0 Object\test_images"

image_paths = []
for ext in ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.webp"):
    image_paths.extend(glob.glob(os.path.join(test_folder, ext)))

model.predict(image_paths, conf=0.25, save=True)
