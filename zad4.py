import cv2
import numpy as np

image = cv2.imread("image1.jpg")
B, G, R = cv2.split(image)

R_boosted = cv2.add(R, 50)
merged_boosted_red = cv2.merge([B, G, R_boosted])
cv2.imshow("Boosted Red Channel", merged_boosted_red)

G_boosted = cv2.add(G, 50)
merged_boosted_green = cv2.merge([B, G_boosted, R])
cv2.imshow("Boosted Green Channel", merged_boosted_green)

cv2.waitKey(0)
cv2.destroyAllWindows()