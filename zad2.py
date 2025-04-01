import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)


height = image.shape[0]
half_height = height // 2

upper_half = image[0:half_height, :]
lower_half = image[half_height:, :]
lower_half[:] = (0, 255, 0)

cv2.imshow('Dolna połowa obrazu', lower_half)
cv2.waitKey(0)
cv2.destroyAllWindows()

half_image = image.copy()

cv2.imshow('Oryginalny obraz', half_image)
cv2.waitKey(0)
cv2.destroyAllWindows()