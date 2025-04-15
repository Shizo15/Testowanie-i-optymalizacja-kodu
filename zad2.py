import cv2
import matplotlib.pyplot as plt

image = cv2.imread('binarny.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

results = []
iterations = [1, 2, 3]
for i in iterations:
    dilated = cv2.dilate(gray, None, iterations=i)
    results.append(dilated)

plt.figure(figsize=(15, 5))
for i in range(len(iterations)):
    plt.subplot(1, 3, i+1)
    plt.imshow(results[i], cmap='gray')
    plt.title(f'Dylatacja {iterations[i]} iteracje')
plt.show()