import cv2
import numpy as np

image = cv2.imread("image.jpg")

height, width = image.shape[:2]

tx = width // 2 + 50
ty = height // 2 + 50

M = np.float32([[1, 0, tx], [0, 1, ty]])

shifted_image = cv2.warpAffine(image, M, (width, height))

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Przesuniety obraz", shifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
