import cv2
import numpy as np

image = cv2.imread("image.jpg")

B, G, R = cv2.split(image)

cv2.imshow("Original", image)
cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)

cv2.imwrite("blue_channel.jpg", B)
cv2.imwrite("green_channel.jpg", G)
cv2.imwrite("red_channel.jpg", R)

cv2.waitKey(0)
cv2.destroyAllWindows()