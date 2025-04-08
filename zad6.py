import cv2
import numpy as np

image = cv2.imread("image1.jpg")

B, G, R = cv2.split(image)

merged_swapped = cv2.merge([R, G, B])
cv2.imshow("Blue-Red Swapped", merged_swapped)

G_zero = G.copy()
G_zero[:] = 0
merged_no_green = cv2.merge([B, G_zero, R])
cv2.imshow("No Green Channel", merged_no_green)

R_zero = R.copy()
R_zero[:] = 0
merged_no_red = cv2.merge([B, G, R_zero])
cv2.imshow("No Red Channel", merged_no_red)

cv2.waitKey(0)
cv2.destroyAllWindows()