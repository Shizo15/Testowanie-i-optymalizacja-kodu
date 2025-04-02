import cv2
import numpy as np

image = cv2.imread('image.jpg')

dark_numpy = image - 80
M = np.ones(image.shape, dtype="uint8") * 80
dark_opencv = cv2.subtract(image, M)

cv2.imshow('NumPy', dark_numpy)
cv2.imshow('OpenCV', dark_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()
