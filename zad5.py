import cv2
import numpy as np

image = cv2.imread("image.jpg")

tx = int(input("Podaj przesunięcie w poziomie (tx): "))
ty = int(input("Podaj przesunięcie w pionie (ty): "))

M = np.float32([[1, 0, tx], [0, 1, ty]])

shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Oryginalny obraz", image)
cv2.imshow(f"Przesuniety obraz (tx={tx}, ty={ty})", shifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
