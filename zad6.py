import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]


center_x, center_y = w // 2, h // 2
half_size = 50

top_left = (center_x - half_size, center_y - half_size)
bottom_right = (center_x + half_size, center_y + half_size)

cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), -1)

cv2.imshow("Obraz po zmianie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()