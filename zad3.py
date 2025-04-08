import cv2
import numpy as np

image = cv2.imread("image1.jpg")
B, G, R = cv2.split(image)

merged_rbg = cv2.merge([R, B, G])
cv2.imshow("RBG Swapped", merged_rbg)

B_zero = B.copy()
B_zero[:] = 0
merged_no_blue = cv2.merge([B_zero, G, R])
cv2.imshow("No Blue Channel", merged_no_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()