import cv2
import numpy as np


image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

center = (0, 0)


rotation_matrix = cv2.getRotationMatrix2D(center, 30, 1.0)

cos = np.abs(rotation_matrix[0, 0])
sin = np.abs(rotation_matrix[0, 1])
new_w = int((h * sin) + (w * cos))
new_h = int((h * cos) + (w * sin))

rotation_matrix[0, 2] += (new_w / 2) - center[0]
rotation_matrix[1, 2] += (new_h / 2) - center[1]

rotated_image = cv2.warpAffine(image, rotation_matrix, (new_w, new_h))

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Obrocony obraz wzgledem lewego gornego naroznika', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()