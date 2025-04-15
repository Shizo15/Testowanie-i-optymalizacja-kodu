import cv2
import matplotlib.pyplot as plt

test_image = cv2.imread('word.jpg')
_, binary = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY_INV)

operations = [
    ('Erozja', cv2.MORPH_ERODE),
    ('Dylatacja', cv2.MORPH_DILATE),
    ('Otwarcie', cv2.MORPH_OPEN),
    ('Zamknięcie', cv2.MORPH_CLOSE),
    ('Gradient', cv2.MORPH_GRADIENT)
]

kernels = [
    ('Kwadrat', cv2.MORPH_RECT, (5, 5)),
    ('Krzyż', cv2.MORPH_CROSS, (5, 5)),
    ('Elipsa', cv2.MORPH_ELLIPSE, (5, 5))
]

plt.figure(figsize=(20, 20))
for i, (op_name, op_code) in enumerate(operations):
    for j, (ker_name, ker_shape, ker_size) in enumerate(kernels):
        kernel = cv2.getStructuringElement(ker_shape, ker_size)
        result = cv2.morphologyEx(binary, op_code, kernel)

        plt.subplot(len(operations), len(kernels), i * len(kernels) + j + 1)
        plt.imshow(result, cmap='gray')
        plt.title(f'{op_name} ({ker_name})')
plt.tight_layout()
plt.show()

# Erozja i dylatacja mają przeciwne efekty
# Otwarcie usuwa małe obiekty i wygładza kontury
# Zamknięcie wypełnia dziury
# Gradient morfologiczny podkreśla krawędzie obiektów.
# Kształt kernela wpływa na sposób przetwarzania