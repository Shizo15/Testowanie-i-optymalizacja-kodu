import cv2
import imutils


image = cv2.imread("image.jpg")

shifted_image = imutils.rotate(image, 75)
cv2.imwrite("rotated_output.jpg", shifted_image)


cv2.imshow("Obrocony obraz o 90", shifted_image)

cv2.waitKey(0)