import cv2
import numpy as np

image = cv2.imread('image.jpg')

roi = image[70:260, 320:480]

roi[:] = (0, 255, 0)

image_with_roi = image.copy()

cv2.imshow('Obraz z zaznaczonym ROI', image_with_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

