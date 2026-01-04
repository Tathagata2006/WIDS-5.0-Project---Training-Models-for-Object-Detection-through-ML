import cv2
import numpy as np

#Section A: Image Processing Basics

#Question 1.

#Loading
img = cv2.imread('Opencv_tut/New folder/bird.jpg')

cv2.imshow('bird', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray-bird', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#gaussianblur
Gblur = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow('Gblur-bird', Gblur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Canny Edge Detect
edges = cv2.Canny(Gblur, 50, 150)

cv2.imshow('Edged-bird', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Question 2.

#Rotate (by 90,say)
roated_bird = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Bird_R_90', roated_bird)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Resize Image
bird_resized_1 = cv2.resize(img, (400, 400))
bird_resized_2 = cv2.resize(img, (0, 0), fx = 0.8, fy = 0.8)
bird_resized_3 = cv2.resize(img, (0, 0), fx = 1.5, fy = 0.6)

cv2.imshow('bird_rs_1', bird_resized_1)
cv2.imshow('bird_rs_2', bird_resized_2)
cv2.imshow('bird_rs_3', bird_resized_3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Flip (H and V)
bird_flip_H = cv2.flip(img, 1)
bird_flip_V = cv2.flip(img, 0)

cv2.imshow('flipH', bird_flip_H)
cv2.imshow('flipV', bird_flip_V)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Question 5.

#Binary thresholding
binary_bird = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('binaryth', binary_bird[1])
cv2.waitKey(0)
cv2.destroyAllWindows()

#Adaptive Thresholding
adaptive_bird = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Adaptiveth', adaptive_bird)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Otsu's thresholding
otsu_bird = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Otsuth", otsu_bird[1])
cv2.waitKey(0)
cv2.destroyAllWindows()

#Question 6.

#Contour detection
contours, hierarchy = cv2.findContours(binary_bird[1], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#draw contours
contour_bird = img.copy()
cv2.drawContours(contour_bird, contours, -1, (0, 255, 0), 2)

cv2.imshow('Countourimg', contour_bird)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Number of contours
print("the number of detected contours :", len(contours)) #Result = 23