import cv2
import numpy as np

image = cv2.imread('image.jpg')

roi = image[100:400, 100:400]

cv2.imwrite('cropped_image.jpg', roi)

cv2.imshow("asd",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()