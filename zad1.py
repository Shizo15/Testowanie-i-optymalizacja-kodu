import numpy as np
import cv2

def draw_triangle(image, pts, color=255):
    return cv2.fillPoly(image, [pts], color)

image_size = (300, 300)
triangle = np.zeros(image_size, dtype="uint8")
circle = np.zeros(image_size, dtype="uint8")

triangle_pts = np.array([[25, 275], [150, 25], [275, 275]])
draw_triangle(triangle, triangle_pts)

cv2.circle(circle, (200, 150), 100, 255, -1)

cv2.imshow("Triangle", triangle)
cv2.imshow("Circle", circle)

bitwise_and = cv2.bitwise_and(triangle, circle)
bitwise_or = cv2.bitwise_or(triangle, circle)
bitwise_xor = cv2.bitwise_xor(triangle, circle)
bitwise_not_triangle = cv2.bitwise_not(triangle)

cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("XOR", bitwise_xor)
cv2.imshow("NOT Triangle", bitwise_not_triangle)

cv2.waitKey(0)
cv2.destroyAllWindows()