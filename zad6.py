import cv2
import numpy as np

image = cv2.imread('image.jpg')

roi = image[70:170, 320:420].copy()

image_with_roi = image.copy()

cv2.imshow('Obraz z zaznaczonym ROI', image_with_roi)
cv2.waitKey(0)

image_with_pasted_roi = image.copy()
image_with_pasted_roi[200:300, 100:200] = roi

cv2.imshow('Obraz z wklejonym ROI', image_with_pasted_roi)
cv2.waitKey(0)

cv2.imshow('Wycięty ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()