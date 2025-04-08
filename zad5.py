import cv2
import numpy as np

image = cv2.imread("image1.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

B, G, R = cv2.split(image)
R = cv2.add(R, 100, mask=mask)
merged_modified = cv2.merge([B, G, R])

cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Modified Red Channel", merged_modified)

cv2.waitKey(0)
cv2.destroyAllWindows()