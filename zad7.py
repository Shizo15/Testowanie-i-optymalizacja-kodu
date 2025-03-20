import cv2
import imutils
import numpy as np


image = cv2.imread("image.jpg")
angle = 60

shifted_image = imutils.rotate(image, angle)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, angle, 1.0)

rotated_cv2 = cv2.warpAffine(image, M, (w, h))

rotated_cv2_rgb = cv2.cvtColor(rotated_cv2, cv2.COLOR_BGR2RGB)

cv2.imshow("Obrocony obraz - imutils", shifted_image)
cv2.imshow("Obrocony obraz - cv2.warpAffine", rotated_cv2)

cv2.waitKey(0)
