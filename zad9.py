import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

image[50:100, 50:100] = (255, 255, 255)

cv2.imshow("asd", image)
cv2.waitKey(0)