import cv2
import numpy as np

image = cv2.imread("image3.jpg")

mask = np.zeros(image.shape[:2], np.uint8)
mask[500:1400, 400:1200] = 255  
background = cv2.bitwise_and(image, image, mask=~mask)
blurred_bg = cv2.GaussianBlur(background, (25, 25), 0)
foreground = cv2.bitwise_and(image, image, mask=mask)
result = cv2.add(foreground, blurred_bg)

cv2.imshow("Depth of Field", result)
cv2.waitKey(0)