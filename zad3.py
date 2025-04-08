import cv2
import numpy as np

image = cv2.imread("car2.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

result = cv2.bitwise_and(image, image, mask=mask)

darkened = image.copy()
darkened[mask == 0] = darkened[mask == 0] // 4

cv2.imshow("Original Image", image)
cv2.imshow("Color Mask", mask)
cv2.imshow("Extracted Color", result)
cv2.imshow("Darkened Other Colors", darkened)
cv2.waitKey(0)
cv2.destroyAllWindows()