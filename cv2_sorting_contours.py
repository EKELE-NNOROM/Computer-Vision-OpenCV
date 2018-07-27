import cv2
import numpy as np

def get_contour_areas(contours):
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

# Load our image
image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/bunchofshapes.jpg")
cv2.imshow('0 - Original Image', image)

# Create a blank image with same dimensions as our loaded image
blank_image = np.zeros((image.shape[0], image.shape[1], 3))

# Create a copy of our original image
original_image = image

# Grayscale of our image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 50, 200)
cv2.imshow('1 - Canny Edges', edged)
opened = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, (3,3))
cv2.imshow("Open", opened)

# Find contours and print how many were found
im2, contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours found = " +  str(len(contours)))

# Draw all contours over blank image
cv2.drawContours(blank_image, contours, -1, (0,255,0), 3)
cv2.imshow('2 - All Contours over blank image', blank_image)

# Draw all contours
cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow('3 - All Contours', image)

# Let's print the areas of the contours before sorting
print("Contour Areas before sorting")
print(get_contour_areas(contours))

# Sort contours large to small
sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)
# sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]

print("Contour Areas after sorting")
print(get_contour_areas(sorted_contours))

# Iterate over our contours and draw one at a time
for c in sorted_contours:
    cv2.drawContours(original_image, [c], -1, (255,0,0), 3)
    cv2.imshow('Contours by area', original_image)

cv2.waitKey()
cv2.destroyAllWindows()
