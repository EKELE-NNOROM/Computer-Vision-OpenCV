import cv2
import numpy as np

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/input.jpg")

# Other Option to Rotate
img = cv2.transpose(image)

cv2.imshow('Rotated Image - Method 2', img)
cv2.waitKey()
cv2.destroyAllWindows()
