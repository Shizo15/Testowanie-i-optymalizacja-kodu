import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)

roi = image[0:100, 0:100]

roi[:] = (0, 255, 0)

image_with_roi = image.copy()

cv2.imshow('Obraz z zaznaczonym ROI', image_with_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Sam ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()