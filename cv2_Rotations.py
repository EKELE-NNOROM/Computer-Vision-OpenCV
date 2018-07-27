import cv2
import numpy as np

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/input.jpg")

# Store height and width of the image
height, width = image.shape[:2]


# Divide by two to rotate the image around its center
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)

# We use warpAffine to transform the image using the matrix, T
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()
