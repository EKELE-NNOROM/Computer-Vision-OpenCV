import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0,180, 255, -1)
cv2.imshow("Ellipse", img)
cv2.waitKey()
cv2.destroyAllWindows()
