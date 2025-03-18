import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

center = (150,150)
size = 20
for r in range(5):
    half_size = size // 2  
    top_left = (center[0] - half_size, center[1] - half_size)
    bottom_right = (center[0] + half_size, center[1] + half_size)

    cv2.rectangle(canvas, top_left, bottom_right, (255, 255, 255), 2)

    size += 20

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)