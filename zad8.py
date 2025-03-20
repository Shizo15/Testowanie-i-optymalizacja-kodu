import cv2
import imutils


image = cv2.imread("image.jpg")
angle = 30

shifted_image = imutils.rotate(image, angle)
shifted_image2 = imutils.rotate(image, angle*2)
shifted_image3 = imutils.rotate(image, angle*3)

single_shift = imutils.rotate(image, 90)


cv2.imshow("Obrocony obraz o 30", shifted_image)
cv2.imshow("Obrocony obraz o 30 po raz drugi", shifted_image2)
cv2.imshow("Obrocony obraz o 30 po raz trzeci", shifted_image3)
cv2.imshow("Obrocony obraz o 90", shifted_image3)

cv2.waitKey(0)