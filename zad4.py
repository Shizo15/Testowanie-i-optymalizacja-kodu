import cv2
import matplotlib.pyplot as plt

broken_image = cv2.imread('word.jpg')
_, binary = cv2.threshold(broken_image, 127, 255, cv2.THRESH_BINARY_INV)

kernels = [
    ('Prostokąt', cv2.MORPH_RECT, (5, 5)),
    ('Elipsa', cv2.MORPH_ELLIPSE, (5, 5)),
    ('Krzyż', cv2.MORPH_CROSS, (5, 5))
]
results = []
for name, shape, size in kernels:
    kernel = cv2.getStructuringElement(shape, size)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    results.append((name, closing))

plt.figure(figsize=(15, 5))
plt.subplot(141), plt.imshow(binary, cmap='gray'), plt.title('Oryginał')
for i in range(len(results)):
    plt.subplot(1, 4, i+2)
    plt.imshow(results[i][1], cmap='gray')
    plt.title(f'Zamknięcie ({results[i][0]})')
plt.show()