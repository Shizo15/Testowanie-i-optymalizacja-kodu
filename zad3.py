import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

resized = cv2.resize(image, (300, 200), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Resized", resized)
cv2.waitKey(0)