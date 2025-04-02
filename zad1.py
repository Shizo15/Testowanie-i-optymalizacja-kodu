import cv2
import numpy as np

image = cv2.imread('image.jpg')

bright_numpy = image + 50

M = np.ones(image.shape, dtype="uint8") * 50
bright_opencv = cv2.add(image, M)

cv2.imshow('Original', image)
cv2.imshow('NumPy', bright_numpy)
cv2.imshow('OpenCV', bright_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()
