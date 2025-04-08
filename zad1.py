import cv2
import numpy as np

image = cv2.imread("image.jpg")

cv2.imshow("Original Image", image)

mask = np.zeros(image.shape[:2], dtype="uint8")

(x, y, w, h) = (90, 30, 70, 80)
cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

cv2.imshow("Face Mask", mask)

masked_face = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Masked Face", masked_face)
cv2.waitKey(0)
cv2.destroyAllWindows()