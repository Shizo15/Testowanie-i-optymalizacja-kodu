import cv2

image = cv2.imread("image.jpg")

blur_simple = cv2.blur(image, (5, 5))

blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

blur_median = cv2.medianBlur(image, 5)

blur_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow("Original", image)
cv2.imshow("Simple Blur", blur_simple)
cv2.imshow("Gaussian Blur", blur_gaussian)
cv2.imshow("Median Blur", blur_median)
cv2.imshow("Bilateral Blur", blur_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1b: Odpowiedzi
# i. Najlepiej usuwa szum: metoda medianowa (skuteczna przeciwko szumowi impulsowemu).
# ii. Najwięcej szczegółów zachowuje: rozmycie dwustronne (nie rozmywa krawędzi).
# iii. Zalety/Wady:
# - cv2.blur: Szybkie, ale rozmazuje krawędzie.
# - cv2.GaussianBlur: Naturalne rozmycie, ale wolniejsze.
# - cv2.medianBlur: Usuwa szum impulsowy, ale nie działa dobrze na duże jądra.
# - cv2.bilateralFilter: Zachowuje krawędzie, ale bardzo wolne dla dużych parametrów.