import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# Drawing a blue line with thickness 5 pixels
line = cv2.line(img, (0,0), (511,511), (255,0,0), 5)

# Drawing a green square with thickness 3 pixels
square = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Drawing a red circle
circle = cv2.circle(img, (447, 63), 63, (0,0,255), 1)
#cv2.imshow("Line", line)
#cv2.imshow("Rectangle", square)
cv2.imshow("Circle", circle)
cv2.waitKey()
cv2.destroyAllWindows()
