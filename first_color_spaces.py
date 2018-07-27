import cv2
import numpy as np

image = cv2.imread('/home/ebuka/Documents/Mastering Computer vision/images/input.jpg')

hsv_image = cv2.cvtColor(image, cv2.colorBGR2_HSV)
cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue Channel', hsv_image[:, :, 0])
cv2.imshow('Saturation Channel', hsv_image[:, :, 1])
cv2.imshow('Value Channel', hsv_image[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()
