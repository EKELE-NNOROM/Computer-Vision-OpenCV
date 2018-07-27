import cv2
import numpy as np

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/elephant.jpg")
cv2.imshow('Original', image)

# Box filter
blur = cv2.blur(image, (3,3))
cv2.imshow('Averaging', blur)

# Gaussian Kernel
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)

# Median Filter
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)

# Bilateral Filter
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey()
cv2.destroyAllWindows()
