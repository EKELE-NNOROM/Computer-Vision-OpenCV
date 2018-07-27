import cv2
import numpy as np

def x_cord_contours(contours):
    # Returns the X coordinate for the contour centroid
    if cv2.contourArea(contours) > 10:
        M = cv2.moments(contours)
        return (int(M['m10']/M['m00']))

def label_contour_center(image,c):
    # Places a red circle on the centers of the contours
    M = cv2.moments(contours)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    
    # Draw the circle on the image
    cv2.circle(image, (cx, cy), 10, (0,0,255), -1)
    return image
    

# Load our image
image = cv2.imread("/home/ebuka/Documents/Mastering Computer vision/images/bunchofshapes.jpg")
cv2.imshow('0 - Original Image', image)

# Create a blank image with same dimensions as our loaded image
blank_image = np.zeros((image.shape[0], image.shape[1], 3))

# Create a copy of our original image
original_image = image.copy()

# Grayscale of our image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 50, 200)
cv2.imshow('1 - Canny Edges', edged)

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
#print("Contour Areas before sorting")
#print(get_contour_areas(contours))

# Sort contours large to small
#sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)
# sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]

#print("Contour Areas after sorting")
#print(get_contour_areas(sorted_contours))

# Iterate over our contours and draw one at a time
#for c in sorted_contours:
 #   cv2.drawContours(original_image, [c], -1, (255,0,0), 3)
  #  cv2.imshow('Contours by area', original_image)

# Compute center of mass or centroids and draw them on our image
for i,c in enumerate(contours):
    orig = label_contour_center(image, c)

cv2.imshow('4 - Contour Centers', image)
cv2.waitKey()

# Sort by left to right using our x_cord_contour function
contours_left_to_right = sorted(contours, key=x_cord_contour, reverse = False)

# Labelling contours left to right
for i,c in enumerate(contours_left_to_right):
    cv2.drawContours(original_image,[c], -1, (0,0,255), 3)
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.putText(original_image, str(i+1), (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow('6 - Left to Right Contour', original_image)
    (x,y,w,h) = cv2.boundingRect(c)

    # Let's now crop each contour and save these images
    cropped_contour = original_image[y:y+h, x:x+w]
    image_name = 'output_shape_number_' + str(i+1) + '.jpg'
    print image_name
    cv2.imwrite(image_name, cropped_contour)

cv2.destroyAllWindows()
