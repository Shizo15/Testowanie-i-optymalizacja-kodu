import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)


width = image.shape[1]
half_width = width // 2

left_half = image[:, :half_width]
right_half = image[:, half_width:]
right_half[:] = (0, 255, 0)

cv2.imshow('Prawa połowa obrazu', right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()

half_image = image.copy()

cv2.imshow('Oryginalny obraz', half_image)
cv2.waitKey(0)
cv2.destroyAllWindows()