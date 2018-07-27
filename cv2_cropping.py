import cv2
import numpy as np

image = cv2.imread('/home/ebuka/Documents/Mastering Computer vision/images/input.jpg')
height, width = image.shape[:2]

# Let's get the starting pixel coordinates (top left of cropping rectangle)
start_row, start_col = int(height * 0.25), int(width * 0.25)

# Let's get the ending pixel coordinates (bottom right of cropping rectangle)
end_row, end_col = int(height * 0.75), int(width * 0.75)

# Simply use indexing to crop out the rectangle we desire
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped)
cv2.waitKey()
cv2.destroyAllWindows()
