import cv2
import imutils
import numpy as np


image = cv2.imread("image.jpg")

shifted_image = imutils.translate(image, 100, 50)

M = np.float32([[1, 0, 100], [0, 1, 50]])

shifted_warpAffine = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Przesuniety obraz - imutils", shifted_image)
cv2.imshow("Przesuniety obraz - cv2.warpAffine", shifted_warpAffine)

cv2.waitKey(0)
