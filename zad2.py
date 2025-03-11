import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Przed zmianą", image)
cv2.waitKey(0)

image[h-1, w-1] = (0, 0, 255)
(b, g, r) = image[h-1, w-1]
print("\nPrzed zmianą: ")
print("Pixel at (525, 800) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image = cv2.imread('image.jpg')
cv2.imshow("Po zmianie", image)
cv2.waitKey(0)

(b, g, r) = image[h-1, w-1]
print("\nPo zmianie: ")
print("Pixel at (525, 800) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
