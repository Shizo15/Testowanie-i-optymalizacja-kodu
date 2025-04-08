import cv2
import numpy as np

image = cv2.imread("image.jpg")

output = image.copy()

left_eye = (108, 60, 12, 5)
right_eye = (135, 60, 12, 5)

cv2.rectangle(output, (left_eye[0], left_eye[1]),
              (left_eye[0] + left_eye[2], left_eye[1] + left_eye[3]),
              (0, 0, 0), -1)
cv2.rectangle(output, (right_eye[0], right_eye[1]),
              (right_eye[0] + right_eye[2], right_eye[1] + right_eye[3]),
              (0, 0, 0), -1)


cv2.imshow("Original", image)
cv2.imshow("Hidden Eyes", output)
cv2.waitKey(0)
cv2.destroyAllWindows()