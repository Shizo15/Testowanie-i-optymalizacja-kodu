import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

(b, g, r) = image[50, 50]
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[200, 200]
print("Pixel at (200, 200) - Red: {}, Green: {}, Blue: {}".format(r, g, b))