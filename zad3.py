import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Image", image)
cv2.waitKey(0)

(cX, cY) = (w // 2, h // 2)

(b, g, r) = image[cX, cY]
print("Pixel at (262, 400) - Red: {}, Green: {}, Blue: {}".format(r, g, b))