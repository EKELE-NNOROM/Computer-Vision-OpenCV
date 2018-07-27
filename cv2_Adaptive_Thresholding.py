import cv2
import numpy as np

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/Origin_of_Species.jpg", 0)

cv2.imshow('Original', image)

ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)

# It's good practice to blur images as it removes noise
image = cv2.GaussianBlur(image, (3,3), 0)

# Using adaptive Threshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 3, 5)
cv2.imshow('Adaptive Mean Thresholding', thresh)

_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", thresh)

blur = cv2.GaussianBlur(image, (7,7), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Gaussian Otsu's Thesholdin", thresh)
cv2.waitKey()
cv2.destroyAllWindows()
