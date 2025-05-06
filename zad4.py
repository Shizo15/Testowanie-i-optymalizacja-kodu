import cv2

text_image = cv2.imread("image1.jpg")
blurred = cv2.blur(text_image,(5,5))
blurred_median = cv2.medianBlur(text_image,5)
blurred_gaussian = cv2.GaussianBlur(text_image, (15, 15), 0)
blurred_bilateral = cv2.bilateralFilter(text_image, 9, 75, 75)

cv2.imshow("Blur", blurred_gaussian)
cv2.waitKey(0)

cv2.imshow("Median", blurred_gaussian)
cv2.waitKey(0)

cv2.imshow("Gaussian", blurred_gaussian)
cv2.waitKey(0)

cv2.imshow(f"Bilateral", blurred_bilateral)
cv2.waitKey(0)

# 4c: Odpowiedzi
# i. Najmocniej rozmywają: cv2.blur i cv2.GaussianBlur.
# ii. Czytelność zachowuje: cv2.medianBlur i cv2.bilateralFilter.