import cv2
import numpy as np

template = cv2.imread('/home/ebuka/Documents/Mastering Computer vision/images/4star.jpg', 0)
cv2.imshow('Template', template)

target = cv2.imread('/home/ebuka/Documents/Mastering Computer vision/images/shapestomatch.jpg')
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(template, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

im2, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

sort_contours = sorted(contours, key=cv2.contourArea, reverse=True)
template_contour = contours[1]

im3, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    match = cv2.matchShapes(template_contour, c, 3, 0.0)
    print(match)

    if match < 0.15:
        closest_contour = c
    else:
        closest_contour = []

cv2.drawContours(target, [closest_contour], -1, (0,255,0), 3)
cv2.imshow('Output', target)
cv2.waitKey(0)
cv2.destroyAllWindows()
