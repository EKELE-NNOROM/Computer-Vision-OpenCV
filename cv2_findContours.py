import cv2
import numpy as np

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/shapes.jpg")
cv2.imshow('Input Image', image)

# Gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find canny edges
ret, thresh = cv2.threshold(gray, 127, 255, 0)

# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Canny Edges After Contouring', im2)


print('Number of Contours found = ' + str(len(contours)))

# Draw all contours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow('Contours', image)
cv2.waitKey()
cv2.destroyAllWindows()
