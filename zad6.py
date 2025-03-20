import cv2
import imutils
import numpy as np


image = cv2.imread("image.jpg")

rotated_image = imutils.rotate_bound(image, -33)


cv2.imshow("Przesuniety obraz - imutils", rotated_image)

cv2.waitKey(0)
