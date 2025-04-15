import cv2
import matplotlib.pyplot as plt

image = cv2.imread('noise.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_sizes = [(3, 3), (5, 5), (7, 7)]
results = []
for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    results.append(opening)

plt.figure(figsize=(15, 5))
plt.subplot(141), plt.imshow(gray, cmap='gray'), plt.title('Oryginał')
for i in range(len(kernel_sizes)):
    plt.subplot(1, 4, i+2)
    plt.imshow(results[i], cmap='gray')
    plt.title(f'Otwarcie {kernel_sizes[i]}')
plt.show()