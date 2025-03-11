import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

part_h, part_w = h // 3, w // 3

start_x, start_y = part_w, part_h
end_x, end_y = 2 * part_w, 2 * part_h

center_part = image[start_y:end_y, start_x:end_x]

cv2.imshow("Środkowy fragment", center_part)
cv2.waitKey(0)


