import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/scan.jpg")

cv2.imshow('Original', image)

# Coordinates of the 4 corners of the original image
points_A = np.float32([[320,15],[700,215],[85,610],[530,780]])

# Coordinates of the 4 corners of the desired output
points_B = np.float32([[0,0],[420,0],[0,594],[420,594]])

# Use the two sets of four points to compute
# the Perspective Transformation matrix, M
M = cv2.getPerspectiveTranform(points_A, points_B)

warped = cv2.warpPerspective(image, M, (420,594))

cv2.imshow('Warp Perspective', warped)
cv2.waitKey()
cv2.destroyAllWindows()


