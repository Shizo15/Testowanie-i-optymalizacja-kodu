import numpy as np
import cv2

image1 = np.zeros((300, 300, 3), dtype="uint8")
image2 = np.zeros((300, 300, 3), dtype="uint8")

cv2.rectangle(image1, (50, 50), (250, 250), (255, 0, 0), -1)
cv2.rectangle(image2, (50, 50), (250, 250), (255, 0, 0), -1)
cv2.circle(image1, (150, 150), 50, (0, 255, 0), -1)
cv2.circle(image2, (170, 150), 50, (0, 255, 0), -1)


diff = cv2.bitwise_xor(image1, image2)

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Differences (XOR)", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()