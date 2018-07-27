import numpy as np
import cv2

# Load image and keep a copy
image = cv2.imread('/home/ebuka/Documents/Mastering Computer vision/images/house.jpg')
orig_image = image.copy()
cv2.imshow('Original Image', orig_image)

# Grayscale and binarize
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
im2, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Iterate through each contour (c) and compute the bounding rectangle
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(orig_image, (x,y), (x+w, y+h), (0,0255), 2)
    cv2.imshow('Bounding Rectangle', orig_image)

# Iterate through each contour (c) and compute the approx contour
for c in contours:
    # Calculate accuracy as a percent of the contour perimeter
    accuracy = 0.03 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0, (0,255,0), 2)
    cv2.imshow('Approx Poly DP', image)

cv2.waitKey()
cv2.destroyAllWindows()
