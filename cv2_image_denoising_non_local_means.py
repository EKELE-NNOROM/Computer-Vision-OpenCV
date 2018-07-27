import numpy as np
import cv2

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/elephant.jpg")

# Parameters, after None are - filter strength 'h' (5-10 is a good range)
# Next is hForColorComponents, set as same value as h again

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow('Original', image)
cv2.imshow('Fast Means Denoising', dst)
cv2.waitKey()

cv2.destroyAllWindows()
