import cv2

image = cv2.imread("image.jpg")

kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

for k in kernel_sizes:
    blurred = cv2.blur(image, k)
    cv2.imshow(f"Blur k={k}", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for k in kernel_sizes:
    blurred = cv2.GaussianBlur(image, k, 0)
    cv2.imshow(f"Gaussian Blur k={k}", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for k in kernel_sizes:
    blurred = cv2.medianBlur(image, k[0])
    cv2.imshow(f"Median blur k={k}", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()

diameters = [5, 9, 15]

for d in diameters:
    blurred = cv2.bilateralFilter(image, d, 75,75)
    cv2.imshow(f"Bilateral d={d}", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# 2b: Odpowiedzi w komentarzach
# i. Większy kernel = silniejsze rozmycie, ale utrata detali.
# ii. Optymalny rozmiar: 5x5 lub 9x9 (zależy od obrazu).