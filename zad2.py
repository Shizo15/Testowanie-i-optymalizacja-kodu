import cv2
import numpy as np

image = cv2.imread('image.jpg')

burned_numpy = image + 150
M = np.ones(image.shape, dtype="uint8") * 150
burned_opencv = cv2.add(image, M)

cv2.imshow('NumPy', burned_numpy)
cv2.imshow('OpenCV', burned_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()
