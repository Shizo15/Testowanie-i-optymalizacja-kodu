import cv2
import imutils

image = cv2.imread('image.jpg')

rotated_image = imutils.rotate(image, angle=180)

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Obrocony obraz o 180 stopni', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()