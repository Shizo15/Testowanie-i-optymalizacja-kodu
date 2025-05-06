import cv2
import numpy as np

image = cv2.imread("image.jpg")

noise = np.zeros(image.shape, np.uint8)
cv2.randn(noise, 0, 50)
noisy_image = cv2.add(image, noise)

blurred = cv2.blur(image,(5,5))
denoised_median = cv2.medianBlur(noisy_image, 5)
denoised_gaussian = cv2.GaussianBlur(noisy_image, (5, 5), 0)
blurred_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Ocena: Mediana lepsza dla szumu impulsowego, Gauss dla szumu gaussowskiego.