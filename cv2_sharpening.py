import cv2
import numpy as np

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/input.jpg")
cv2.imshow('Original', image)

# Sharpening kernel
kernel_sharpening = np.array([[-1, -1,-1],
                              [-1, 9, -1],
                              [-1, -1, -1]])

# applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imshow('Image Sharpening', sharpened)

cv2.waitKey()
cv2.destroyAllWindows()
