import cv2
import os

input = "chocolates"
output = "blur_output"

os.makedirs(output, exist_ok = True)

#gaussian blur + lowlight -> all images 


for filename in os.listdir(input) :
    path = os.path.join(input, filename)
    img = cv2.imread(path)
    
    if img is None :
        continue
    
    name, ext = os.path.splitext(filename)
    
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    low_light = cv2.convertScaleAbs(blur, alpha=0.4, beta=0)
    
    new_filename = name + "_blur" + ext
    
    newpath = os.path.join(output, new_filename)
    cv2.imwrite(newpath, low_light)
    
print("done.")