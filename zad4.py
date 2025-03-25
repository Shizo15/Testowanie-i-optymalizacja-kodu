import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

flipped = cv2.flip(image, 0)
cv2.imshow("Odbicie poziome", flipped)

flipped2 = cv2.flip(image, 1)
cv2.imshow("Odbicie pionowe", flipped2)

flipped2 = cv2.flip(flipped, 1)
cv2.imshow("Odbicie względem obu osi", flipped2)

cv2.waitKey(0)