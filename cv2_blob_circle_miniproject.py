import cv2
import numpy as np

image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/blobs.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Create a detector with default parameters
detector = cv2.SimpleBlobDetector_create()

# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1,1))

blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255),
                          cv2.DRAW_MATCHES_FLAGS_DEFAULT)

number_of_blobs = len(keypoints)
text = "Total number of Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,0,255), 2)

# Show blobs
cv2.imshow("Blobs using default parameters", blobs)
cv2.waitKey(0)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True
params.minArea = 100

# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.9

# Set Covexity filtering parameters
params.filterByConvexity = False
params.minConvexity = 0.2

# Set Inertia filtering paramters
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the above parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,100,255), 2)

# Show blobs
cv2.imshow('Filtering Circular Blobs Only', blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
