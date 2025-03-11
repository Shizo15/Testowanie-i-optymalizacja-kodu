import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

image[100, 0:w] = (0,255,0)

cv2.imshow("asd", image)
cv2.waitKey(0)