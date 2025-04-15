import cv2
import matplotlib.pyplot as plt

plate = cv2.imread('tablica1.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(plate, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)

plt.figure(figsize=(15, 5))
plt.subplot(131), plt.imshow(plate, cmap='gray'), plt.title('Oryginał')
plt.subplot(132), plt.imshow(binary, cmap='gray'), plt.title('Binaryzacja')
plt.subplot(133), plt.imshow(closing, cmap='gray'), plt.title('Po przetwarzaniu')
plt.show()