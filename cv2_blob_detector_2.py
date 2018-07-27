import cv2
import numpy as np

im = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/Sunflowers.jpg", cv2.IMREAD_GRAYSCALE)

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create()


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
