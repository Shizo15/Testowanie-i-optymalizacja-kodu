import cv2
import numpy as np

image = cv2.imread("image1.jpg")
B, G, R = cv2.split(image)

zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Blue (B)", cv2.merge([B, zeros, zeros]))
cv2.imshow("Green (G)", cv2.merge([zeros, G, zeros]))
cv2.imshow("Red (R)", cv2.merge([zeros, zeros, R]))

print("Analiza kanałów:")
print("- Obiekty czerwone są najjaśniejsze w kanale R")
print("- Obiekty zielone są najjaśniejsze w kanale G")
print("- Obiekty niebieskie są najjaśniejsze w kanale B")

cv2.waitKey(0)
cv2.destroyAllWindows()